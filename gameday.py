#!/usr/bin/python
import sms
from sms import asciify
from datetime import datetime
from os import environ

#module constants and templates
API_CLIENT = "SEATGEEK_CLIENT_ID"
API_SECRET = "SEATGEEK_CLIENT_SECRET"
WARRIORS_PARAM = 'golden-state-warriors&venue.slug=oracle-arena'
ATHLETICS_PARAM = 'oakland-athletics&venue.slug=oakland-coliseum'
RAIDERS_PARAM = 'oakland-raiders&venue.slug=oakland-coliseum'
META = 'meta'
TOTAL = 'total'
EVENTS = 'events'
SHORT_TITLE = 'short_title'
DATETIME_LOCAL = 'datetime_local'
SINGLE_UNDERSCORE = "_"
DOUBLE_UNDERSCORE = "__"
AT = " @"
BASE_TEMPLATE = 'https://api.seatgeek.com/2/events?sort=score.desc&performers.slug={team}{date}{auth}'
DATE_TEMPLATE = '&datetime_local.gte={year}-{month}-{day}T{hour}:{minute}:{second}&datetime_local.lte={year}-{month}-{day}T23:59:49'
AUTH_TEMPLATE = "&client_id={client_id}&client_secret={client_secret}"
SMS_TEMPLTE = "Game Alert! {game_data} \n-data via SeatGeek"


#ensure access to seatgeek API auth info
client_id = environ.get(API_CLIENT, None)
client_secret = environ.get(API_SECRET, None)
assert client_id != None , "Could not find seatgeek client_id in environment variables"
assert client_secret != None, "Could not find seatgeek client_secret in environment variables"

#get current date/time and normalize
current_time = datetime.now()

year   = str(current_time.year)
month  = str(current_time.month).zfill(2)
day    = str(current_time.day).zfill(2)
hour   = str(current_time.hour).zfill(2)
minute = str(current_time.minute).zfill(2)
second = str(round(current_time.second,2)).zfill(2)

#compose date and auth components of URL
date_params = DATE_TEMPLATE.format(year = year, month = month, day = day, hour = hour, minute = minute, second = second)
auth_params = AUTH_TEMPLATE.format(client_id = client_id, client_secret = client_secret)

#init smtp server
server = sms.SMTPServer()

#collect team info from seatgeek 
events = {}
for team_params in [WARRIORS_PARAM, RAIDERS_PARAM, ATHLETICS_PARAM]:
	api = BASE_TEMPLATE.format(team = team_params, date = date_params, auth = auth_params)

	try:
		data = sms.request(api)
		count = data[META][TOTAL]
		if count > 0: 
			title = data[EVENTS][0][SHORT_TITLE]
			time = data[EVENTS][0][DATETIME_LOCAL][-8:-3]
			events[title] = time

	except(sms.urllib2.HTTPError, sms.urllib2.URLError) as e:
		server.logError(str(e) + '\n + from gameday.py')

#decide if sms needs to be sent out
if len(events) > 0:
	game_data = []
	for title, time in events.items():
		message = str(title) + AT + str(time)
		game_data.append(message)

	#send message
	sms_message = SMS_TEMPLTE.format('\n'.join(game_data))
	server.sendText('parth', sms_message)
#clean up
server.quit()







