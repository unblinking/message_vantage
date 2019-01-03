#!/usr/bin/perl -w

# message vantage - edit message 2
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

require "../lib/mv_subs.lib";	# relative location of common subroutines file from cgi
my $dir = '../messages';		# relative location of messages directory from cgi

my $filename = param('filename');
my $message_body = '';

open(MESSAGEBODY, "$dir/$filename") or die "Error opening message file\n Cannot open message file $dir/$filename\n $!\n";
while (<MESSAGEBODY>)	{				# read message file contents into a variable
	$message_body .= "$_";
}
close (MESSAGEBODY) or die "Error closing message file\n Cannot close message file $dir/$filename\n $!\n";

$filename =~ s/ //gi;					# remove spaces from timestamp
$filename =~ s/DATE/-/gi;				# remove date label from timestamp
$filename =~ s/TIME//gi;				# remove time label from timestamp
$filename =~ s/\-\d*\D*$//gi;			# remove the timestamp from the filename

print header;
&message_composition ($filename, $message_body);
