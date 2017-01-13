import cherrypy
import twilio.twiml
import wikipedia
"""
This has not been maintained since it relies on the
cherrpy server receiving a request from twilio's 
request-url-via-SMS service. My free trial twilio
number has long expired.
"""


#constants 
WIKI = 'wiki'

class Root(object):
        @cherrypy.expose
        def index(self,Body, **params):
                if type(Body) == list:
                        Body = Body[0]
                Body = str(Body).lower()
                resp = twilio.twiml.Response()
                wikiSearch = len(Body.split(WIKI)) > 1
                if wikiSearch:
                        output = wikipedia.summary(wikipedia.search(Body.split(WIKI)[1].strip()), 1)
                        resp.message(output)
                        return str(resp)

                else:
                        resp.message("Please prefix search with wiki: such as wiki Obama")
                        return str(resp)
