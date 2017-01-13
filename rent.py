#!/usr/bin/python
import sms
from sms import asciify
from random import randint
from os import environ

#module constants and templates
DEFAULT_NAME = "HEY"
NICKNAMES = "NICKNAMES"
MESSAGE_TEMPLATE = "{}, pay that rent $$$!"

#initailize smpt
server = sms.SMTPServer()

#parse message
nicknames = environ.get(NICKNAMES, DEFAULT_NAME).split()
nickname = nicknames[randint(0,len(nicknames) -1)]

#send text
message = MESSAGE_TEMPLATE.format(nickname)
server.sendText('nikita', message)
server.sendText('parth', message)
#clean up
server.quit()
