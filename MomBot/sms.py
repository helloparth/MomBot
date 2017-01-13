#!/usr/bin/python
import urllib2
import json
import smtplib
import configs
from twilio.rest import TwilioRestClient
from os import environ

#constants
GMAIL_AUTH = 'GMAIL_AUTH'
DEBUG_LEVEL = 1
GMAIL_SMTP_SERVER = 'smtp.gmail.com'
GMAIL_SMTP_PORT = 587
AT = "@"

"""
SMTP Server for sending SMS messages
via SMS Gateway.

Command Line Usage:
> from sms import SMTPServer
> server = SMTPServer()
> server.sendText("parth", "Sup dude?")
"""
class SMTPServer(object):
	"""smtp server for momBot messaging"""

	def __init__(self):
		"""authenticate with GMAIL SMTP server"""
		self.__server = smtplib.SMTP(GMAIL_SMTP_SERVER,GMAIL_SMTP_PORT)
		self.__server.starttls()
		self.__server.login(configs.MY_EMAIL, environ[GMAIL_AUTH])
		self.__server.set_debuglevel(DEBUG_LEVEL)

	def sendText(self,user, message):
		"""sends message"""
		self.__server.sendmail(configs.MY_EMAIL,configs.CONTACTS[user], message)

	def quit(self):
		"""terminate smtp server"""
		self.__server.quit()

	def logError(self, errorMessage):
		"""Sends error messages back to configs.MY_EMAIL address"""
		self.__server(configs.MY_EMAIL, errorMessage)

"""
Twilio Server for sending SMS messages. 
"""
class TwillioServer(object):

	def __init__(self):
		"""set up initial twilio rest client"""
		self.__server = TwilioRestClient()
		self.__hostNumber = configs.TWILIO_HOST_NUMBER

	def sendText(self, user, message):
		"""sends message"""
		message = '\n ' + message
		senderNumber = configs.CONTACTS[user].split(AT)[0]
		self.__server.messages.create(to=senderNumber, from_=self.__hostNumber,body=message)
	
	def quit(self):
		"""terminate smtp server"""
		pass
	def logError(self, errorMessage):
		self.__server.messages.create(to=configs.MY_NUMBER, from_=self.__hostNumber, body=errorMessage)


def asciify(string):
	"""replaces all non ascii unicode characeters with a period"""
	string = str(string)
	return ''.join([i if ord(i) < 128 else '.' for i in string])

def request(url):
	"""returns json response  from a synchronous call to url"""
	return json.loads(urllib2.urlopen(url).read())

