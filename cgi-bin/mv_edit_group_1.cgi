#!/usr/bin/perl -w

# message vantage - edit group 1
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

require "../lib/mv_subs.lib";	# relative location of common subroutines file from cgi
my $dir = '../subscribers';	# relative location of subscriber directory from cgi
my $filename = 'subscribers.dat';	# filename of subscriber records

my $groups = '';

foreach (unique_existing_groups($dir,$filename))	{	# build html form of existing groups
	$groups .= "<span style=\"background: #ccc;\"><input type=\"radio\" name=\"selected_group\" id=\"selected_group\" value=\"$_\" onclick=\"EditGroup2()\" />$_</span> &nbsp\; &nbsp\;";
}

print header;
&edit_group_1;

sub edit_group_1	{
print <<"EOFEOF";
<form id="edit_group_1">	<!-- begin edit group 1 form -->
<fieldset>
	<legend>Edit Group</legend>
	<p>
		Check the radio button to the left of the group to be edited.
	</p>
	$groups
</fieldset>
</form>	<!-- end edit group 1 form -->
EOFEOF
}
