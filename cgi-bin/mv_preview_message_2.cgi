#!/usr/bin/perl -w

# mv - preview message 2
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

require "../lib/mv_subs.lib";	# relative location of common subroutines file from cgi
my $dir = '../messages';		# relative location of messages directory from cgi

my $filename = param('filename');
my $fakecfn = param('fakecfn');
my $fakecln = param('fakecln');
my $fakecea = param('fakecea');

my $body = '';

open(MESSAGE, "$dir/$filename") or die "Error reading message file\n Cannot open message file $dir/$filename\n $!\n";
while (<MESSAGE>)	{		# find and replace special variable names to personalize each email
	$_ =~ s/CFNCFN/$fakecfn/g;
	$_ =~ s/CLNCLN/$fakecln/g;
	$_ =~ s/CEACEA/$fakecea/g;
	$body .= "$_";
}
close (MESSAGE) or die "Error closing message file\n Cannot open message file $dir/$filename\n $!\n";

print header;

if (param('format') eq 'html')	{
	&notify_box("HTML Preview","$body");
}

if (param('format') eq 'text')	{
	&notify_box("TEXT Preview","<textarea rows=\"20\" cols=\"60\" readonly=\"readonly\">$body</textarea>");
}
