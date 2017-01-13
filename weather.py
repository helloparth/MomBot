#!/usr/bin/python
import sms
from sms import asciify
from os import environ

#module constants and templates
WEATHER_ENDPOINT= 'http://api.openweathermap.org/data/2.5/weather?zip=94105,USA&units=imperial&APPID={}'
API_KEY = 'WEATHER_API_KEY'
WEATHER = 'weather'
DESCRIPTION = 'description'
RAIN = 'rain'
MAIN = 'main'
TEMP = 'temp'
MESSAGE_TEMPLATE = "SF is {} degrees and the weather is {}."
RAIN_TEMPLATE = "\nIt rained {} in the past 3 hrs."


#ensure you have open weather API key in env vars
key = environ.get(API_KEY, None)
assert key != None , "Could not find WEATHER_API_KEY in environment variables."
open_weather_api = WEATHER_ENDPOINT.format(key)

#initialize smtp server
server = sms.SMTPServer()
weather_data = sms.request(open_weather_api)

try:
	#parse out relevant fields
	weather = asciify(weather_data[WEATHER][0][DESCRIPTION])
	rain = asciify(weather_data.get(RAIN, '{}'))
	temp = asciify(str(weather_data[MAIN][TEMP]))

	#stitch message
	message = MESSAGE_TEMPLATE.format(temp, weather)
	if rain != '{}': 
		message += RAIN_TEMPLATE.format(rain)

	#send message via sms
	server.sendText('parth', message)	

except(sms.urllib2.HTTPError, sms.urllib2.URLError) as e:
	server.logError(str(e) + '\n + from weather.py')

#clean up
server.quit()
