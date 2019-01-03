#!/usr/bin/perl -w

# message vantage - edit group 2
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

my $selected_group = param('selected_group');

print header;
&edit_group_2;

sub edit_group_2 {
print <<"EOFEOF";
<form id="edit_group_2">	<!-- begin edit group 2 form -->
<fieldset>
	<p>
		Rename the existing group
		<br /><input name="old_name" id="old_name" size="50" value="$selected_group" disabled />
		<br />as
		<br /><input name="new_name" id="new_name" size="50" value="$selected_group" />
	</p>
</fieldset>
<fieldset>
	<p>
		<b><a href="#" onclick="EditGroup3();clearTarget2();setTimeout('EditGroup1()', 2000)">SAVE NEW GROUP NAME</a></b>
	</p>
</fieldset>
</form>	<!-- end edit group 2 form -->
EOFEOF
}
