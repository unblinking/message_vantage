#!/usr/bin/perl -w

# message vantage - delete subscriber 2
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

my $record = param('record');

(my $last, my $first, my $email, my $groups) = split(/\|/,$record,4);	# split record into separate variables

print header;
&delete_subscriber;

sub delete_subscriber	{
print <<"EOFEOF";
<form id="delete_subscriber_2">	<!-- begin form -->
<input name="record" id="record" type="hidden" size="50" value="$record" />
<fieldset>
	<legend>Delete Existing Subscriber</legend>
	<table>
		<tr><td>First Name</td><td><input name="first_name" id="first_name" size="50" value="$first" disabled /></td></tr>
		<tr><td>Last Name</td><td><input name="last_name" id="last_name" size="50" value="$last" disabled /></td></tr>
		<tr><td>Email Address</td><td><input name="email_address" id="email_address" size="50" value="$email" disabled /></td></tr>
		<tr><td>Group(s)</td><td><input name="groups" id="groups" size="50" value="$groups" disabled /></td></tr>
	</table>
</fieldset>
<fieldset>
	<legend>Are You Sure?</legend>
	<p>Are you absolutely sure you want to permanently delete the selected subscriber record?</p>
	<b><a href="#" onclick="DeleteSubscriber3(); clearTarget2(); setTimeout('DeleteSubscriber1()', 2000)">YES, DELETE SUBSCRIBER RECORD</a></b>
</fieldset>
</form>	<!-- end form -->
EOFEOF
}
