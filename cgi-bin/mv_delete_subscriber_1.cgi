#!/usr/bin/perl -w

# message vantage - delete subscriber 1
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

my $dir = '../subscribers';	# relative location of subscriber directory from cgi
my $filename = 'subscribers.dat';	# filename of subscriber records

my $records = '';

&read_records;
print header;
&list_records;

sub read_records	{
open (SUBSCRIBERS, "$dir/$filename") or die "Error reading existing subscriber records\n Cannot open subscriber file at $dir/$filename\n $!\n";
	while (<SUBSCRIBERS>)	{
		chomp ($_);																			# remove end of record marker newline
		(my $last, my $first, my $email, my $groups) = split(/\|/,$_,4);	# split record into separate variables
		if ($email ne '')	{																# build html table of subscriber records
			$records .= "<tr class=\"customers\"><td><input name=\"record\" id=\"record\" type=\"radio\" value=\"$_\" onclick=\"DeleteSubscriber2()\" /></td><td>$last</td><td>$first</td><td>$email</td><td>$groups</td></tr>\n";
		}
	}
close (SUBSCRIBERS) or die "Error closing existing subscriber records\n Cannot close subscriber file at $dir/$filename\n $!\n";
}

sub list_records	{
print <<"EOFEOF";
<form id="delete_subscriber_1">	<!-- begin delete subscriber 1 form -->
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
		$records
	</table>
</fieldset>
</form>	<!-- end delete subscriber 1 form -->
EOFEOF
}
