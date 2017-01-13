#!/usr/bin/python
import sms
from sms import asciify

#module constants and templates
INSPIRATION_ENDPOINT = 'http://quotes.rest/qod.json'
CONTENTS = "contents"
QUOTES = "quotes"
QUOTE = "quote"
AUTHOR = "author"
MESSAGE_TEMPLATE = "{} \n- {}"

#initialize smtp server
server = sms.SMTPServer()
inspiration_data = sms.request(INSPIRATION_ENDPOINT)

try: 
	#parse out relevant fields
	quote = asciify(inspiration_data[CONTENTS][QUOTES][0][QUOTE])
	author = asciify(inspiration_data[CONTENTS][QUOTES][0][AUTHOR])

	#stitch message
	message = MESSAGE_TEMPLATE.format(quote,author)

	#send message via sms
	server.sendText('parth', message)

except (sms.urllib2.HTTPError, sms.urllib2.URLError) as e:
	server.logError(str(e) + '\n from inspiration.py')

#clean up
server.quit()
