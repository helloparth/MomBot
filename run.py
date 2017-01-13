#!/usr/bin/python
from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def hello_world():
	"""Respond to incoming calls with a text messaging"""
	resp = twilio.twiml.Response()
	resp.message("This feature is currently unsupported. Check us out at github.com/helloparth/MomBot.")
	return str(resp)
if __name__=="__main__": 
	app.run(debug=True)
