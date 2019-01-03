#!/usr/bin/perl -w

# message vantage - delete group 1
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

require "../lib/mv_subs.lib";	# relative location of common subroutines file from cgi
my $dir = '../subscribers';	# relative location of subscriber directory from cgi
my $filename = 'subscribers.dat';	# filename of subscriber records

my $groups_table = '';

foreach (&unique_existing_groups($dir,$filename))	{	# build html form of existing group names
	$groups_table .= "<span style=\"background: #ccc;\"><input type=\"radio\" name=\"delete_group\" id=\"delete_group\" value=\"$_\" onclick=\"DeleteGroup2()\" />$_</span> &nbsp\; &nbsp\;";
}

print header;
&list_groups;

sub list_groups {
print <<"EOFEOF";
<form id="delete_group_1">	<!-- begin delete group 1 form -->
<fieldset>
	<legend>Delete Group</legend>
	<p>
		Check the radio button to the left of the group to be permanently deleted.
	</p>
	$groups_table
</fieldset>
</form>	<!-- end delete group 1 form -->
EOFEOF
}
