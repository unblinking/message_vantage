#!/usr/bin/perl -w

# message vantage - create group 2
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

require "../lib/mv_subs.lib";	# relative location of common subroutines file from cgi
my $dir = '../subscribers';	# relative location of subscriber directory from cgi
my $filename = 'subscribers.dat';	# filename of subscriber records

my $new_groups = param('new_groups');
my $final_groups = '';

$new_groups = (lc $new_groups);											# convert new group names to lower case
$new_groups =~ s/ //g;														# remove spaces from new group names
my @new_groups = split(/,/,$new_groups);								# load new group names into an array
@new_groups = do { my %seen; grep !$seen{$_}++, @new_groups };	# remove duplicate elements in array
@new_groups = grep /\S/, @new_groups;									# remove empty elements in array
@new_groups = sort(@new_groups);											# sort array

foreach (@new_groups)	{
	$final_groups .= "$_,";													# format the elements to use in the subscriber record. all group names separated by commas
}


print header;
if ($new_groups =~ /[^A-Za-z0-9\,\_\-]/)	{	# verify subscriber groups are valid characters
	&notify_box("Invalid Group Name","At least one group name in the groups you entered, <b>$final_groups</b>, contain(s) illegal characters. Please revise the group name(s) to contain letters, numerals, hyphens, or underscores only, with each group name separated by a comma.");
}	else	{
	my $record = "|||$final_groups";							# format record to store group names only
	&new_subscriber_record($dir,$filename,$record);		# save record to file
	&notify_box("New Group(s) Saved","Group(s) <b>$final_groups</b> successfully saved.");
}
