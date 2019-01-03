#!/usr/bin/perl -w

# message vantage - edit subscriber 1
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

my $dir = '../subscribers';	# relative location of subscriber directory from cgi
my $filename = 'subscribers.dat';	# filename of subscriber records

my $records_table = '';

&build_records;
print header;
&list_records;

sub build_records	{
open (SUBSCRIBERS, "$dir/$filename") or die "Cannot open subscriber file at $dir/$filename : $!\n";
	while (<SUBSCRIBERS>)	{
		chomp ($_);																			# remove end of record marker newline
		(my $last, my $first, my $email, my $groups) = split(/\|/,$_,4);	# split record into separate variables
		if ($email ne '')	{																# build html table of existing subscriber records
			$records_table .= "<tr class=\"customers\"><td><input name=\"subscriber_record\" id=\"subscriber_record\" type=\"radio\" value=\"$_\" onclick=\"EditSubscriber2()\" /></td><td>$last</td><td>$first</td><td>$email</td><td>$groups</td></tr>\n";
		}
	}
close (SUBSCRIBERS);
}

sub list_records	{
print <<"EOFEOF";
<form id="edit_subscriber_1">	<!-- begin edit subscriber 1 form -->
<fieldset>
	<legend>Existing Subscribers</legend>
	<table>
		<tr class="customers">
			<th></th>
			<th><b>LAST NAME</b></th>
			<th><b>FIRST NAME</b></th>
			<th><b>EMAIL ADDRESS</b></th>
			<th><b>SUBSCRIBED GROUPS</b></th>
		</tr>
		$records_table
	</table>
</fieldset>
</form>	<!-- end edit subscriber 1 form -->
EOFEOF
}
