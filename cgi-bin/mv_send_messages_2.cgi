#!/usr/bin/perl -w

# message vantage - send messages 2
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

require "../lib/mv_subs.lib";							# relative location of common subroutines file from cgi
my $default_from_email = 'josh@joshgray.com';		# default from email address if none provided
my $default_from_name = 'Joshua Gray';					# default from email name if none provided

my @to_groups = param('to_groups');		# groups selected to be emailed
my $from_name = param('from_name');		# company name to appear as from email name
my $from_email = param('from_email');	# company email to appear as from email address
my $subject = param('subject');			# email subject line
my $mfilename = param('mfilename');		# email message body filename
my $groups_table = '';

if ($from_name eq '')	{$from_name = "$default_from_name";}
if ($from_email eq '')	{$from_email = "$default_from_email";}

@to_groups = sort (@to_groups);
foreach (@to_groups)	{						# build html form of selected group names
	if ($_ ne '')	{
		$groups_table .= "<span style=\"background: #ccc;\"><input type=\"checkbox\" name=\"to_groups\" id=\"to_groups\" value=\"$_\" disabled checked />$_</span> &nbsp\; &nbsp\;";
	}
}

print header;
if ($from_name =~ /[^A-Za-z0-9\ \_\-\.]/)	{			# verify from name is valid characters
	&notify_box("Invalid From Name","The email <b>From Name</b> name you entered, <b>$from_name</b>, contains illegal characters. Please revise the From Name to contain letters, numerals, hyphens, or underscores only.");
}	elsif (&bad_email_address_format($from_email)){	# verify from email is valid format
	&notify_box("Invalid Email Address","The <b>From Email Address</b> you entered, <b>$from_email</b>, is not a valid email address format. Please correct the email address and try again.");
}	elsif ($subject =~ /[^A-Za-z0-9\ \,\.\_\-\!]/)	{	# verify subject is valid characters
	&notify_box("Invalid Email Subject Line","The <b>Email Subject Line</b> name you entered, <b>$subject</b>, contains illegal characters. Please revise the Email Subject Line to contain letters, numerals, spaces, commas, periods, hyphens, or underscores only.");
}	elsif	($groups_table eq '')	{						# verify groups table is not null
	&notify_box("No Groups Selected","You failed to select any groups. Please select at least one group and try again.");
}	else	{
	&messages_ready;
}

sub messages_ready {
print <<"EOFEOF";
<form id="send_messages_2">	<!-- begin send messages 2 form -->
<fieldset>
	<legend>Messages Ready To Send</legend>
	<p>
		The messages are ready to be sent as follows
		<br /><b>From:</b><br /><input name="from_name" id="from_name" size="50" value="$from_name" readonly disabled />
		<br /><b>From Email Address:</b><br /><input name="from_email" id="from_email" size="50" value="$from_email" readonly disabled />
		<br /><b>Email Subject Line:</b><br /><input name="subject" id="subject" size="50" value="$subject" readonly disabled />
		<br /><b>Selected Groups:</b><br />$groups_table
		<br /><b>Saved Message Name:</b><br /><input name="mfilename" id="mfilename" size="50" value="$mfilename" readonly disabled />
	</p>
</fieldset>
<fieldset>
	<p>
		<b><a href="#" onclick="SendMessages3(); clearTarget1()">SEND ALL MESSAGES NOW</a></b>
	</p>
</fieldset>
</form>	<!-- end send messages 2 form -->
EOFEOF
}
