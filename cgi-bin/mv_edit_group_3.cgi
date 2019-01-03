#!/usr/bin/perl -w

# message vantage - edit group 3
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

require "../lib/mv_subs.lib";	# relative location of common subroutines file from cgi
my $dir = '../subscribers';	# relative location of subscriber directory from cgi
my $filename = 'subscribers.dat';	# filename of subscriber records

my $old_name = param('old_name');
my $new_name = param('new_name');

my $new_file = '';

$new_name =~ s/ //g;				# remove spaces
$new_name = (lc $new_name);	# convert all characters to lower case
if ($new_name eq '')	{			# keep old name if new name equals null
	$new_name = $old_name;
}

print header;

if ($new_name =~ /[^A-Za-z0-9_]/)	{	# verify new group name is valid characters
	&notify_box("Invalid Group Name","The group name $new_name contain(s) illegal characters. Please revise the group name to contain letters, numerals, or underscores only.");
}	else	{
	&build_edited_file;
	&save_edited_file;
	&notify_box("Group Changed","The group <b>$old_name</b> was permanently changed to <b>$new_name</b> for all current subscribers.");
}

sub save_edited_file	{
open (SUBSCRIBERS, ">$dir/$filename") or die "Can't open subscriber file at $dir/$filename : $!\n";
print SUBSCRIBERS "$new_file";
close (SUBSCRIBERS);
}

sub build_edited_file	{
open (SUBSCRIBERS, "$dir/$filename") or die "Cannot open subscriber file at $dir/$filename : $!\n";
	while (<SUBSCRIBERS>)	{
		chomp $_;																			# remove end of record marker newline
		(my $last, my $first, my $email, my $groups) = split(/\|/,$_,4);	# split record into separate variables
		$groups =~ s/$old_name/$new_name/g;											# replace occurrences of old group name with new group name
		my $new_record = "$last|$first|$email|$groups";							# build record with edited groups
		$new_file .= "$new_record\n";													# build file contents with edited records
	}
close (SUBSCRIBERS);
}
