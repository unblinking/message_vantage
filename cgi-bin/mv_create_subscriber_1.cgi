#!/usr/bin/perl -w

# message vantage - create subscriber 1
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

require "../lib/mv_subs.lib";	# relative location of common subroutines file from cgi
my $sdir = '../subscribers';	# relative location of subscriber directory from cgi
my $sfilename = 'subscribers.dat';	# filename of subscriber records

my $group_options = '';

foreach (&unique_existing_groups($sdir,$sfilename))	{	# build html drop down list options of existing group names
	$group_options .= "<option value=\"$_\">$_</option>";
}

print header;
&create_subscriber_form;

sub create_subscriber_form	{
print <<"EOFEOF";
<form id="create_subscriber_1">	<!-- begin create subscriber 1 form -->
<fieldset>
	<legend>New Subscriber Details</legend>
	<p>
		 Enter the new subscriber <b>First Name</b>, <b>Last Name</b>, and <b>Email Address</b>. To create new groups for this subscriber, enter the new group names separated by commas in the <b>New Groups</b> field.
	</p>
	<table>
		<tr><td>First Name</td><td><input name="first_name" size="50" /></td></tr>
		<tr><td>Last Name</td><td><input name="last_name" size="50" /></td></tr>
		<tr><td>Email Address</td><td><input name="email_address" size="50" /></td></tr>
		<tr><td>New Group(s)</td><td><input name="new_groups" size="50" /></td></tr>
	</table>
</fieldset>
<fieldset>
	<legend>Select Existing Groups</legend>
	<p>
		You may also select pre-existing groups for the new subscriber. To select pre-existing groups, click the group name in the menu on the left side and then click <b>Add</b>. Selected groups will then be displayed in the menu on the right side.
	</p>
	<table>	<!-- begin existing group options table -->
		<tr>
			<td>
				Possible Groups
			</td>
			<td>
				Chosen Groups
			</td>
		</tr>
		<tr>
			<td>
				<select name="possible_groups" id="possible_groups" size="20" multiple="multiple" style="width: 225px;" ondblclick="copyToList('possible_groups','chosen_groups')">
					$group_options
				</select>
			</td>
			<td>
				<select name="chosen_groups" id="chosen_groups" size="20" multiple="multiple" style="width: 225px;" ondblclick="copyToList('chosen_groups','possible_groups')">
				</select>
			</td>
		</tr>
		<tr>
			<td>
				<input type="button" onclick="copyToList('possible_groups','chosen_groups')" value="Add">
			</td>
			<td>
				<input type="button" onclick="copyToList('chosen_groups','possible_groups')" value="Remove">
			</td>
		</tr>
	</table>	<!-- end existing group options table -->
</fieldset>
<fieldset>
	<b><a href="#" onclick="allSelect('chosen_groups'); CreateSubscriber2()">SAVE NEW SUBSCRIBER</a></b>
</fieldset>
</form>	<!-- end create subscriber 1 form -->
EOFEOF
}
