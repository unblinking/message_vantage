#!/usr/bin/perl -w

# message vantage - send messages 3
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

# i have commented out the ability to actually send emails until testing is complete

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

require "../lib/mv_subs.lib";		# relative location of common subroutines file from cgi
my $sdir = '../subscribers';		# relative location of subscriber directory from cgi
my $mdir = '../messages';			# relative location of messages directory from cgi
my $ldir = '../logs';				# relative location of logs directory from cgi
my $sendmail  = '/usr/sbin/sendmail';	# location of sendmail on the host
my $sfilename = 'subscribers.dat';		# filename of subscriber records
my $opt_out = 'http://www.jmg1138.com/cgi-bin/mv/mv_opt_out_1.cgi';	# http address of opt-out script

my @to_groups = param('to_groups');		# groups selected to be emailed
my $from_name = param('from_name');		# company name to appear as from email name
my $from_email = param('from_email');	# company email to appear as from email address
my $subject = param('subject');			# email subject line
my $mfilename = param('mfilename');		# email message filename

my $mbody = 'Content-Type: text/html; charset=ISO-8859-1';
my $error_report_body_invalid_email_address = '';

my $log_file = &time_stamp;

$mbody .= "\n\n";

open (MBODY, "$mdir/$mfilename") or die "Error reading message file\n Cannot open message file at $mdir/$mfilename\n $!\n";
	while (<MBODY>)	{
		$mbody .= $_;
	}
close (MBODY);

$mbody .= "<br /><br /><form id=\"block_email\" action=\"$opt_out\" method=\"post\"><input name=\"block_email\" id=\"block_email\" type=\"hidden\" value=\"CEACEA\" /><input type=\"submit\" value=\"Unsubscribe\"></form>";

print header;
&create_selected_log_file;
&process_selected_subscribers;
&save_reports;
&notify_box("Messages Sent","All messages have now been sent. For more information see the log files in the message history.");

sub save_reports	{
	open (ERRORREPORT, ">>$ldir/$log_file.errors") or die "Error saving reports\n Cannot open error log file at $ldir/$log_file.errors\n $!\n";
		if ($error_report_body_invalid_email_address)	{
			print ERRORREPORT "INVALID EMAIL ADDRESS ERRORS\n$error_report_body_invalid_email_address\n\n";
		}
	close (ERRORREPORT);
}

sub create_selected_log_file	{
	open (SUBSCRIBERS, "$sdir/$sfilename") or die "Cannot open subscriber file at $sdir/$sfilename : $!\n";
	while (<SUBSCRIBERS>)	{
		chomp ($_);
		(my $last, my $first, my $email, my $groups) = split(/\|/,$_,4);
		if ($email ne '')	{
			my @groups = split(/,/,$groups);
			@groups = do { my %seen; grep !$seen{$_}++, @groups };	# remove duplicates
			open (LOGFILE, ">>$ldir/$log_file.selected.log") or die "Cannot create log file at $ldir/$log_file.selected.log : $!\n";
			if (&dbaSetCommon(\@groups, \@to_groups))	{					# test if two arrays intersect
				print LOGFILE "$_\n";
			}
			close (LOGFILE);
		}
	}
	close (SUBSCRIBERS);
}

sub process_selected_subscribers	{
open (LOGFILE, "$ldir/$log_file.selected.log") or die "Cannot read log file at $ldir/$log_file.selected.log : $!\n";
while (<LOGFILE>)	{
	chomp ($_);
	(my $last, my $first, my $email, my $groups) = split(/\|/,$_,4);
	if (&bad_email_address_format($email)) {
		$error_report_body_invalid_email_address .= "Invalid email $email. No message sent to $first $last.\n";
	} else {
		sleep(10);
		my($psubject,$pbody) = &personalize($last,$first,$email);
#       Sending is disabled here. This is just a demo.
#       Un-comment the next line to allow sending.
#		&send_email($last,$first,$email,$psubject,$pbody);
	}
}
close (LOGFILE);
}

sub personalize {						# find and replace special variable names to personalize each email
	my ($last,$first,$email) = @_;
	my $psubject = $subject;			# start each time with non-personalized email subject line
	$psubject =~ s/CLNCLN/$last/g;
	$psubject =~ s/CFNCFN/$first/g;
	$psubject =~ s/CEACEA/$email/g;
	my $pbody = $mbody;					# start each time with non-personalized email message body
	$pbody =~ s/CLNCLN/$last/g;
	$pbody =~ s/CFNCFN/$first/g;
	$pbody =~ s/CEACEA/$email/g;
	return ($psubject,$pbody);
}

sub send_email {
my ($last,$first,$email,$psubject,$pbody) = @_;
open MAIL, "|$sendmail -oi -t" or die "Error sending email.\n Cannot open pipe to $sendmail\n $!\n";
print MAIL <<"EOFEOF";
To: "$first $last" <$email>
From: "$from_name" <$from_email>
Subject: $psubject
$pbody
EOFEOF
close MAIL or die "Error sending email.\n Cannot close pipe to $sendmail\n $!\n";
}
