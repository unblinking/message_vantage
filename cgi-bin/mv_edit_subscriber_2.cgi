#!/usr/bin/perl -w

# message vantage - edit subscriber 2
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

require "../lib/mv_subs.lib";	# relative location of common subroutines file from cgi
my $sdir = '../subscribers';	# relative location of subscriber directory from cgi
my $sfilename = 'subscribers.dat';	# filename of subscriber records

my $subscriber_record = param('subscriber_record');
my $possible_groups = '';
my $chosen_groups = '';

(my $last, my $first, my $email, my $groups) = split(/\|/,$subscriber_record,4);	# split record into separate variables

my @chosen_groups = split(/,/,$groups);		# load subscribed group names into an array
my @existing_groups = &unique_existing_groups($sdir,$sfilename);


# remove groups from possible list if already subscribed
foreach my $e1 (@existing_groups)	{
	my $count = 0;
	foreach my $e2 (@chosen_groups)	{
		if ($e1 eq $e2)	{
			$count = 1;
		}
	}
	if ($count == 0)	{
		$possible_groups .= "<option value=\"$e1\">$e1</option>";
	}
}

foreach (@chosen_groups)	{	# build html drop down form options for pre-subscribed groups
	$chosen_groups .= "<option value=\"$_\">$_</option>";
}

print header;
if ($subscriber_record eq '')	{		# verify subscriber record is not null
	&notify_box("Please Select A Subscriber","No subscriber was selected. Please select a radio button next to a subscriber record before clicking <b>EDIT SELECTED SUBSCRIBER</b>.");
}	else	{
	&edit_selected_subscriber;
}

sub edit_selected_subscriber	{
print <<"EOFEOF";
<form id="edit_subscriber_2">	<!-- begin edit subscriber 2 form -->
<input name="unedited_record" id="unedited_record" type="hidden" size="50" value="$subscriber_record" />
<fieldset>
	<legend>Existing Subscriber Details</legend>
	<table>
		<tr><td>First Name</td><td><input name="first" id="first" size="50" value="$first" /></td></tr>
		<tr><td>Last Name</td><td><input name="last" id="last" size="50" value="$last" /></td></tr>
		<tr><td>Email Address</td><td><input name="email" id="email" size="50" value="$email" disabled /></td></tr>
		<tr><td>Group(s)</td><td><input name="groups" id="groups" size="50" value="" /></td></tr>
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
					$possible_groups
				</select>
			</td>
			<td>
				<select name="chosen_groups" id="chosen_groups" size="20" multiple="multiple" style="width: 225px;" ondblclick="copyToList('chosen_groups','possible_groups')">
					$chosen_groups
				</select>
			</td>
		</tr>
		<tr>
			<td>
				<input type="button" onclick="copyToList('possible_groups','chosen_groups')" value="Add" />
			</td>
			<td>
				<input type="button" onclick="copyToList('chosen_groups','possible_groups')" value="Remove" />
			</td>
		</tr>
	</table>	<!-- end existing group options table -->
</fieldset>
<fieldset>
	<b><a href="#" onclick="allSelect('chosen_groups'); EditSubscriber3(); clearTarget2(); setTimeout('EditSubscriber1()', 2000)">SAVE EDITED SUBSCRIBER INFO</a></b>
</fieldset>
</form>	<!-- end edit subscriber 2 form -->
EOFEOF
}
