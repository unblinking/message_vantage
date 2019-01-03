#!/usr/bin/perl -w

# message vantage - delete subscriber 3
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

require "../lib/mv_subs.lib";	# relative location of common subroutines file from cgi
my $sdir = '../subscribers';	# relative location of subscriber directory from cgi
my $sfilename = 'subscribers.dat';	# filename of subscriber records

my $record = param('record');
my $remaining_records = '';

&build_edited_file;
&save_edited_file;

print header;
&notify_box("Subscriber Deleted","The subscriber record <br /><b>$record</b><br /> was permanently deleted from the subscriber records file.");

sub build_edited_file	{
open (SUBSCRIBERS, "$sdir/$sfilename") or die "Cannot open subscriber file at $sdir/$sfilename : $!\n";
	while (<SUBSCRIBERS>)	{
		chomp ($_);
		if ($_ eq $record)	{
		}	else	{
		$remaining_records .= "$_\n";
		}
	}
close (SUBSCRIBERS);
}

sub save_edited_file	{
open (SUBSCRIBERS, ">$sdir/$sfilename") or die "Cannot open subscriber file at $sdir/$sfilename : $!\n";
print SUBSCRIBERS "$remaining_records";
close (SUBSCRIBERS);
}
