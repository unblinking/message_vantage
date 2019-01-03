#!/usr/bin/perl -w

# message vantage - delete message 2
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

require "../lib/mv_subs.lib";	# relative location of common subroutines file from cgi
my $dir = '../messages';		# relative location of messages directory from cgi

my $filename = param('filename');
my $sure = param('sure');

print header;
if ($filename eq '')	{	# verify message filename is not null
	&notify_box("No Message Selected","No message was selected. Please <b>select a message</b> before clicking DELETE.");
} else	{
	&sure_or_not;
}

sub sure_or_not	{		# verify user confirmed delete
	if ($sure eq "yes")	{
		unlink("$dir/$filename") or die "Can't delete $dir/$filename\n$!\n";		# delete file
		&notify_box("Message Deleted","Message <b>$filename</b> has been permanently deleted.");
	}	else	{
		&notify_box("Message NOT Deleted","Message <b>$filename</b> was <b>NOT</b> deleted. Verify that you selected the radio button marked <b>YES I am sure</b>.");
	}
}
