#!/usr/bin/perl -w

# message vantage - opt out 1
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

require "../lib/mv_subs.lib";	# relative location of common subroutines file from cgi
my $dir = '../subscribers';	# relative location of subscriber directory from cgi
my $filename = 'subscribers.dat';	# filename of subscriber records

my $block_email = param('block_email');

print header;
print "This would unsubscribe you if it was working by now";
