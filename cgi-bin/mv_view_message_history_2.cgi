#!/usr/bin/perl -w

# message vantage - view message history 2
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

my $dir = '../logs';		# relative location of logs directory from cgi

my $filename = param('filename');
my $log_file = '';

open(LOG, "$dir/$filename") or die "Can't open log file $dir/$filename : $!\n";
while (<LOG>)	{
	$log_file .= $_;
}
close LOG;

print header;
&view_log;

sub view_log {
print <<"EOFEOF";
<fieldset>
	<legend>LOG FILE PREVIEW</legend>
	<textarea rows="20" cols="60" readonly="readonly">$log_file</textarea>
</fieldset>
EOFEOF
}
