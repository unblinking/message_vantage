#!/usr/bin/perl -w

# message vantage - opt out 1
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

my $block_email = param('block_email');

print header;
print "This would unsubscribe $block_email if it was working by now";