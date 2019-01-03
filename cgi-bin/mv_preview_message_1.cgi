#!/usr/bin/perl -w

# mv - preview message 1
# Copyright 2006 Joshua Michael Gray http://www.joshgray.com/

use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

my $dir = '../messages';	# relative location of messages directory from cgi

my $message_list_body = '';

foreach (<$dir/*>)	{				# build html form of existing message filenames
	$_ =~ s!$dir/!!gi;				# remove path from message filename
	$message_list_body .= "<input name=\"filename\" id=\"filename\" type=\"radio\" value=\"$_	\"> $_ <br />\n";
}

print header;
&preview_message_1;

sub preview_message_1	{
print <<"EOFEOF";
<form id="preview_message_1"> <!-- begin preview message 1 form -->
<fieldset>
	<legend>Saved Messages</legend>
	<p>
		Select the radio button to the left of the message, and then click the button at the bottom labeled <b>Preview Selected Message</b>.
	</p>
	$message_list_body
</fieldset>
<fieldset>
	<legend>HTML or TEXT format</legend>
	<p>
		<input name="format" id="format" type="radio" value="html" checked="checked" /> Preview as HTML
		&nbsp; &nbsp; &nbsp;
		<input name="format" id="format" type="radio" value="text" /> Preview as TEXT
	</p>
</fieldset>
<fieldset>
	<legend>Fake Subscriber Info</legend>
	<p>
		If the message uses any special personalization variables, they will be replaced with the following fake demonstration defaults. You may change these values to preview the message with specific names, etc.
	</p>
	<table>	<!-- begin fake subscriber info table -->
		<tr><td>Fake first name</td><td><input name="fakecfn" id="fakecfn" value="John" size="30" /></td></tr>
		<tr><td>Fake last name</td><td><input name="fakecln" id="fakecln" value="Dough" size="30" /></td></tr>
		<tr><td>Fake email address</td><td><input name="fakecea" id="fakecea" value="john_dough\@graydata.com" size="30" /></td></tr>
	</table>	<!-- end fake subscriber info table -->
</fieldset>
<fieldset>
	<p>
		<b><a href="#" onclick="PreviewMessage2()">PREVIEW SELECTED MESSAGE</a></b>
	</p>
</fieldset>
</form>	<!-- end preview message 1 form -->
EOFEOF
}
