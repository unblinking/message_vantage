#!/usr/bin/perl -w

# message vantage - delete group 2
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

my $delete_group = param('delete_group');

print header;
&select_group;

sub select_group {
print <<"EOFEOF";
<form id="delete_group_2">	<!-- begin delete group 2 form -->
<fieldset>
	<p>
		Delete the existing group
		<br /><input name="delete_group" id="delete_group" size="50" value="$delete_group" disabled />
	</p>
</fieldset>
<fieldset>
	<p>
		Before you continue, understand that once the group is deleted there is no way to undelete it.
		<br />
		<br /><b><a href="#" onclick="DeleteGroup3();clearTarget2();setTimeout('DeleteGroup1()', 2000)">PERMANENTLY DELETE EXISTING GROUP</a></b>
	</p>
</fieldset>
</form>	<!-- end delete group 2 form -->
EOFEOF
}
