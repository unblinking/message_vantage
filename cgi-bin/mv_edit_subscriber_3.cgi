#!/usr/bin/perl -w

# message vantage - 
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

require "../lib/mv_subs.lib";		# relative location of common subroutines file from cgi
my $sdir = '../subscribers';		# relative location of subscriber directory from cgi
my $sfilename = 'subscribers.dat';		# filename of subscriber records

my $new_first = param('first');
my $new_last = param('last');
my $new_email = param('email');
my $new_groups = param('groups');
my $unedited_subscriber_record = param('unedited_record');
my @selected_groups = param('chosen_groups');

my $final_groups = '';
my $edited_subscriber_record = '';
my $new_subscriber_file_contents = '';

&prepare_groups;
print header;
if ($new_first =~ /[^A-Za-z0-9\_\-]/)	{					# verify first name is valid characters
	&notify_box("Invalid First Name","The subscriber first name you entered, <b>$new_first</b>, contains invalid characters. Please revise the first name to contain letters, numerals, hyphens, or underscores only.");
}	elsif ($new_last =~ /[^A-Za-z0-9\_\-]/)	{			# verify last name is valid characters
	&notify_box("Invalid Last Name","The subscriber last name you entered, <b>$new_last</b>, contains invalid characters. Please revise the last name to contain letters, numerals, hyphens, or underscores only.");
}	elsif (&bad_email_address_format($new_email))	{	# test if valid email address format
	&notify_box("Invalid Email Address","The email address you entered, <b>$new_email</b>, is not a valid email address format. Please correct the email address and try again.");
}	elsif ($final_groups =~ /[^A-Za-z0-9\,\_\-]/)	{	# test if valid characters
	&notify_box("Invalid Group Name","At least one group name in the groups you entered, <b>$final_groups</b>, contain(s) illegal characters. Please revise the group name(s) to contain letters, numerals, hyphens, or underscores only, with each group name separated by a comma.");
} else	{
	$edited_subscriber_record = "$new_last|$new_first|$new_email|$final_groups";
	&read_old_subscriber_records;
	&overwrite_subscriber_record;
	&notify_box("Subscriber Saved","Subscriber <b>$new_first $new_last</b> has been saved.");
}

sub prepare_groups	{
$new_groups =~ s/ //g;														# remove spaces from new group names
$new_groups = (lc $new_groups);											# force new group names to be lowercase
my @new_groups = split(/,/,$new_groups);								# load new group names into an array
my @all_groups = (@selected_groups,@new_groups);					# combine array elements from existing selected group names and new group names
@all_groups = do { my %seen; grep !$seen{$_}++, @all_groups };	# remove duplicate elements in combined array
@all_groups = grep /\S/, @all_groups;									# remove empty elements in combined array
@all_groups = sort(@all_groups);											# sort array
	foreach (@all_groups)	{
		$final_groups .= "$_,";												# format the list to use in the subscriber record. all group names separated by commas
	}
}

sub read_old_subscriber_records	{
open (SUBSCRIBERS, "$sdir/$sfilename") or die "Can't open subscriber file at $sdir/$sfilename : $!\n";
	while (<SUBSCRIBERS>)	{
		chomp ($_);	# remove end of record marker newline
		if ($_ eq $unedited_subscriber_record)	{
			$_ = $edited_subscriber_record;
		}
		$new_subscriber_file_contents .= "$_\n"
	}
close (SUBSCRIBERS);
}

sub overwrite_subscriber_record	{
open (SUBSCRIBERS, ">$sdir/$sfilename") or die "Can't open subscriber file at $sdir/$sfilename : $!\n";
print SUBSCRIBERS "$new_subscriber_file_contents";
close (SUBSCRIBERS);
}
