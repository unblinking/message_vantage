#!/usr/bin/perl -w

# message vantage - send messages 1
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

require "../lib/mv_subs.lib";	# relative location of common subroutines file from cgi
my $sdir = '../subscribers';	# relative location of subscriber directory from cgi
my $mdir = '../messages';		# relative location of messages directory from cgi
my $sfilename = 'subscribers.dat';	# filename of subscriber records
my $from_name = 'John Dough';
my $from_email = 'john_dough@graydata.com';

my $gselection = '';
my $mselection = '';

foreach (<$mdir/*>)	{
	$_ =~ s!../mv/messages/!!gi;	# remove path from message filename
	$mselection .= "<option value=\"$_\">$_</option>\n";
}

print header;
foreach (&unique_existing_groups($sdir,$sfilename))	{	# build html form of existing group names
	$gselection .= "<span style=\"background: #ccc;\"><input type=\"checkbox\" name=\"to_groups\" id=\"to_groups\" value=\"$_\" />$_</span> &nbsp\; &nbsp\;";	
}

&send_messages;

sub send_messages {
print <<"EOFEOF";
<form id="send_messages_1">	<!-- begin send messages 1 form -->
<fieldset>
	<legend>From</legend>
	<table>
		<tr>
			<td>From Name</td>
			<td><input name="from_name" id="from_name" size="50" value="$from_name" onFocus="value=''" /></td>
		</tr>
		<tr>
			<td>From Email Address</td>
			<td><input name="from_email" id="from_email" size="50" value="$from_email" onFocus="value=''" /></td>
		</tr>
	</table>
</fieldset>
<fieldset>
	<legend>Subject</legend>
	<p>
		It is against federal law to use misleading subject lines in these emails.
	</p>
	<p>
		You can <strong>personalize the email subject line</strong> by using special variable names which will be replaced during script execution. When using these variables, be sure to use all capitalized letters exactly as they appear below. The available variables are:
		<br /> &nbsp; <i>Customer first name: CFNCFN</i>
		<br /> &nbsp; <i>Customer last name: CLNCLN</i>
		<br /> &nbsp; <i>Customer email address: CEACEA</i>
	</p>
	<table>
		<tr>
			<td>Email Subject Line</td>
			<td><input name="subject" id="subject" size="50" value="A special message for CFNCFN CLNCLN." onFocus="value=''" /></td>
		</tr>
	</table>
</fieldset>
<fieldset>
	<legend>To Groups</legend>
	<p>
		Check the boxes to the left of the groups to be emailed.
	</p>
	$gselection
	<p>
		<b><a href="#" onclick="allCheck('send_messages_1','to_groups','true')">Select All Groups</a></b>
		 &nbsp; 
		<b><a href="#" onclick="allCheck('send_messages_1','to_groups','false')">Deselect All Groups</a></b>
	</p>
</fieldset>
<fieldset>
	<legend>Message</legend>
	<p>
		Select the message to be emailed from the drop down list.
	</p>
	<select name=\"mfilename\" id=\"mfilename\">
		$mselection
	</select>
</fieldset>
<fieldset>
	<p>
		<b><a href="#" onclick="SendMessages2()">VALIDATE DATA FOR SENDING MESSAGES</a></b>
	</p>
</fieldset>
</form>	<!-- end send messages 1 form -->
EOFEOF
}
