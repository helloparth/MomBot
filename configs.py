#!/usr/bin/python
from os import environ
"""
You can populate these configs in many ways. I chose to read the from
environment variables. If you are just playing around, you can also set
them explicity such as:

MY_EMAIL  = 'myemail@gmail.com'
MY_NUMBER = '+12345678900'
"""
#gmail address used for GMAIL SMTP
MY_EMAIL  = environ.get("GMAIL_SMTP", "<or hard code your gmail address>@GMAIL.COM")
MY_NUMBER = environ.get("PARTH_NUMBER", "<your number>" )

# Add your contacts here
# Maps a name to SMS gateway address
CONTACTS = {
	'parth':environ.get("PARTH_SMS_GATEWAY", "<your sms gateway address>"),
	'nikita':environ.get("NIKITA_SMS_GATEWAY", "<123456789@vtext.com>"),
	#'john_smith':'123456789@vtext.com'
	}

#Twilio Host Number
TWILIO_HOST_NUMBER = environ.get("TWILIO_HOST_NUMBER", "<your twilio host number>")
