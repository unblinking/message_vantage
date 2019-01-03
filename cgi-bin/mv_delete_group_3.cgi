#!/usr/bin/perl -w

# message vantage - delete group 3
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

require "../lib/mv_subs.lib";	# relative location of common subroutines file from cgi
my $dir = '../subscribers';	# relative location of subscriber directory from cgi
my $filename = 'subscribers.dat';	# filename of subscriber records

my $delete_group = param('delete_group');
my $edited_file = '';

&build_edited_file;
&save_edited_file;

print header;
&notify_box("Group Changed","The group <b>$delete_group</b> was permanently deleted from all current subscribers.");

sub build_edited_file	{
open (SUBSCRIBERS, "$dir/$filename") or die "Cannot open subscriber file at $dir/$filename : $!\n";
	while (<SUBSCRIBERS>)	{
		chomp $_;																			# remove end of record marker newline
		(my $last, my $first, my $email, my $groups) = split(/\|/,$_,4);	# split record into separate variables
		$groups =~ s/$delete_group//g;												# remove occurrences of delete group name from subscribed groups
		my $edited_line = "$last|$first|$email|$groups";						# build record with edited groups
		$edited_file .= "$edited_line\n";											# build file contents with edited records
	}
close (SUBSCRIBERS);
}

sub save_edited_file	{
open (SUBSCRIBERS, ">$dir/$filename") or die "Can't open subscriber file at $dir/$filename : $!\n";
print SUBSCRIBERS "$edited_file";
close (SUBSCRIBERS);
}
