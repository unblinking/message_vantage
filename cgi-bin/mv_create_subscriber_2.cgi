#!/usr/bin/perl -w

# message vantage - create subscriber 2
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

require "../lib/mv_subs.lib";	# relative location of common subroutines file from cgi
my $dir = '../subscribers';	# relative location of subscriber directory from cgi
my $filename = 'subscribers.dat';	# filename of subscriber records

my $first_name = param('first_name');
my $last_name = param('last_name');
my $email_address = param('email_address');
my $new_groups = param('new_groups');
my @selected_groups = param('chosen_groups');

my $final_groups = '';
my $record = '';

my @unique_existing_emails = (&unique_existing_emails($dir,$filename));
my @new_subscriber_email = ($email_address);

&prepare_groups;
print header;

if ($first_name =~ /[^A-Za-z0-9\_\-]/)	{						# verify subscriber first name is valid characters
	&notify_box("Invalid First Name","The subscriber first name you entered, <b>$first_name</b>, contains iillegal characters. Please revise the first name to contain letters, numerals, hyphens, or underscores only.");
}	elsif ($last_name =~ /[^A-Za-z0-9\_\-]/)	{				# verify subscriber last name is valid characters
	&notify_box("Invalid Last Name","The subscriber last name you entered, <b>$last_name</b>, contains illegal characters. Please revise the last name to contain letters, numerals, hyphens, or underscores only.");
}	elsif (&bad_email_address_format($email_address))	{	# verify subscriber email is valid format
	&notify_box("Invalid Email Address","The email address you entered, <b>$email_address</b>, is not a valid email address format. Please correct the email address and try again.");
}	elsif (&dbaSetCommon(\@unique_existing_emails, \@new_subscriber_email))	{	# test if email already exists in subscriber file
	&notify_box("Duplicate Email Address","The email address you entered, <b>$email_address</b>, already exists in the subscriber records. Please edit the existing subscriber record or enter a new email address");
}	elsif ($final_groups =~ /[^A-Za-z0-9\,\_\-]/)	{		# verify subscriber groups are valid characters
	&notify_box("Invalid Group Name","At least one group name in the groups you entered, <b>$final_groups</b>, contain(s) illegal characters. Please revise the group name(s) to contain letters, numerals, hyphens, or underscores only, with each group name separated by a comma.");
}	else	{
	$record = "$last_name|$first_name|$email_address|$final_groups";	# format subscriber record
	&new_subscriber_record($dir,$filename,$record);							# save subscriber record to file
	&notify_box("Subscriber Saved","Subscriber <b>$first_name $last_name</b> has been saved.");
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
