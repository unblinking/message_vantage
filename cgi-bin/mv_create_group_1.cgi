#!/usr/bin/perl -w

# message vantage - create group 1
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

require "../lib/mv_subs.lib";	# relative location of common subroutines file from cgi
my $dir = '../subscribers';	# relative location of subscriber directory from cgi
my $filename = 'subscribers.dat';	# filename of subscriber records

my $groups = '';

foreach (&unique_existing_groups($dir,$filename))	{	# build html list of existing group names
	$groups .= "$_, ";
}

print header;
&create_group_form;

sub create_group_form	{
print <<"EOFEOF";
<form id="create_group_1">	<!-- begin create group 1 form -->
<fieldset>
	<legend>Create A New Group</legend>
	<p>
		Separate new group names by commas. No spaces.
	</p>
	<table>
		<tr>
			<td>New Groups</td>
			<td><input name="new_groups" size="50" /></td>
		</tr>
	</table>
</fieldset>
<fieldset>
	<table>
		<tr class="customers">
			<th>
				<b>List Of Existing Groups</b>
			</th>
		</tr>
		<tr class="customers">
			<td>
				$groups
			</td>
		</tr>
	</table>
</fieldset>
<fieldset>
	<b><a href="#" onclick="CreateGroup2(); setTimeout('CreateGroup1()', 2000)">SAVE NEW GROUP(S)</a></b>
</fieldset>
</form>	<!-- end create group 1 form -->
EOFEOF
}
