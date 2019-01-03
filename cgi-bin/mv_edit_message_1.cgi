#!/usr/bin/perl -w

# message vantage - edit message 1
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

my $dir = '../messages';	# relative location of messages directory from cgi

my @files = <$dir/*>;
my $message_list = '';

foreach (@files)	{					# build html form of existing message filenames
	$_ =~ s!$dir/!!gi;				# remove path from message filename
	$message_list .= "<input name=\"filename\" id=\"filename\" type=\"radio\" value=\"$_\"> $_ <br />\n";
}

print header;
&edit_message;

sub edit_message	{
print <<"EOFEOF";
<form id="edit_message_1">	<!-- begin edit message 1 form -->
<fieldset>
	<legend>Saved Messages</legend>
	<p>
		Select the radio button to the left of the message, and then click the button at the bottom labeled <b>Edit Selected Message</b>.
	</p>
	$message_list
</fieldset>
<fieldset>
	<p>
		<b><a href="#" onclick="EditMessage2()">EDIT SELECTED MESSAGE</a></b>
	</p>
</fieldset>
</form>	<!-- end edit message 1 form -->
EOFEOF
}
