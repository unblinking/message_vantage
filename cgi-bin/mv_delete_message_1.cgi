#!/usr/bin/perl -w

# message vantage - delete message 1
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

my $dir = '../messages';	# relative location of messages directory from cgi

my @files = <$dir/*>;
my $list = '';

foreach (@files)	{					# build html form of existing message filenames
	$_ =~ s!$dir/!!gi;				# remove path from message filename
	$list .= "<input name=\"filename\" id=\"filename\" type=\"radio\" value=\"$_\" /> $_ <br />\n";
}

print header;
&delete_message;

sub delete_message	{
print <<"EOFEOF";
<form id="delete_message_1"> <!-- begin delete message 1 form -->
<fieldset>
	<legend>Delete A Message</legend>
	<p>
		Select the radio button to the left of the message to be deleted</b>.
	</p>
	$list
</fieldset>
<fieldset>
	<legend>Are you SURE?</legend>
	<p>
		Are you really sure that you want to <b>PERMANENTLY DELETE</b> the selected file?
	</p>
	<table>
		<tr>
			<td><input name="sure" id="sure" type="radio" value="yes"></td>
			<td><b>YES</b> I am sure</td>
		</tr>
		<tr>
			<td><input name="sure" id="sure" type="radio" value="no" checked="checked"></td>
			<td><b>NO</b> I am not sure</td>
		</tr>
	</table>
</fieldset>
<fieldset>
	<p>
		<b><a href="#" onclick="DeleteMessage2(); setTimeout('DeleteMessage1()', 2000)">PERMANENTLY DELETE SELECTED MESSAGE</a></b>
	</p>
</fieldset>
</form>	<!-- end delete message 1 form -->
EOFEOF
}
