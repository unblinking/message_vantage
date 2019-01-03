#!/usr/bin/perl -w

# message vantage - view message history 1
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

my $dir = '../logs';	# relative location of logs directory from cgi

my $list = '';

foreach (<$dir/*>)	{
	$_ =~ s!$dir/!!gi;
	$list .= "<option value=\"$_\">$_</option>\n";
}

print header;
&view_logs;

sub view_logs	{
print <<"EOFEOF";
<form id="view_history_1"> <!-- begin form -->
<fieldset>
	<legend>Log Files</legend>
	<p>
		Select the log file to review from the drop down list.
	</p>
	<select name=\"filename\" id=\"filename\"  onchange="ViewHistory2()">
		$list
	</select>
</fieldset>
<fieldset>
	<p>
		<b><a href="#" onclick="ViewHistory2()">VIEW SELECTED LOG</a></b>
	</p>
</fieldset>
</form>	<!-- end form -->
EOFEOF
}
