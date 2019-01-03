#!/usr/bin/perl -w

# message vantage - create message 2
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

require "../lib/mv_subs.lib";	# relative location of common subroutines file from cgi
my $dir = '../messages';		# relative location of messages directory from cgi

my $file = param('message_name');
my $body = param('message_body');

$file =~ s/ /_/g;		# replace spaces with underscores in message filename

print header;
if ($file =~ /[^A-Za-z0-9\_\.]/)	{			# verify message filename is valid characters
	&notify_box("Invalid Message Filename","The message filename <b>$file</b> contains illegal characters. Please revise the message name to contain letters, numerals or underscores only.");
}	elsif ($file eq '')	{						# verify message filename is not null
	&notify_box("No Message Filename","You failed to enter a <b>message filename</b>. Please revise the message file name to contain letters, numerals or underscores only.");
}	elsif ($body eq '')	{						# verify message body is not null
	&notify_box("No Message Body","You failed to enter anything into the message body. You must type a message in the message body before saving.");
}	else	{
	$file .= &time_stamp;						# add time stamp to message filename
	&new_message_file($dir,$file,$body);	# save new message file
	&notify_box("Message Created","Your message, <b>$file</b> has been saved.");
}
