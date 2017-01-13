#!/usr/bin/python
import sms
from sms import asciify
from random import randint
from os import environ

#module constants and templates
DEFAULT_NAME = "HEY"
NICKNAMES = "NICKNAMES"
MESSAGE_TEMPLATE = "{}, don't forget your epipen ;)"

#init smtp server
server = sms.SMTPServer()

#obtain list of possible names
nicknames = environ.get(NICKNAMES, DEFAULT_NAME).split()
nickname = nicknames[randint(0,len(nicknames) -1)]

#send text
message = MESSAGE_TEMPLATE.format(nickname)
server.sendText('parth', message)

#clean up
server.quit()

