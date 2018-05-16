#!/usr/bin/python
import hashlib
import hmac
import time
import os
import urllib
import urllib2

try:
  import simplejson as json
except ImportError:
  import json

class Auth:
  def __init__(self,apiKey):
	self.apiKey = apiKey
	return None
  def hmac(
	self,
	url,
        httpMethod="GET",
        queryParameters=None,
        postData=None):
    timestamp = str(int(round(time.time()*1000)))
    datastring = httpMethod + url
    if queryParameters != None :
        datastring += queryParameters
    datastring += timestamp
    if postData != None :
        datastring += postData
        self.postData = postData
    self.token = hmac.new(self.apiKey.decode('hex'), msg=datastring,digestmod=hashlib.sha256).hexdigest()
    #return token,timestamp
    return self.token,timestamp
  #built-in GET request for REST-API
  def GET(
	self,
	url,
	username,
	httpMethod="GET",
	queryParameters=None,
	postData=None):
	
	token,timestamp = self.hmac(url,httpMethod,queryParameters,postData)
	if queryParameters != None :
	  url = url + "?" + queryParameters
	if postData != None :
		req = urllib2.Request(url, postData)
	else:
		req = urllib2.Request(url)
	req.add_header('Content-Type','application/json')
	req.add_header('Accept','application/json')
	req.add_header('X-LLNW-Security-Principal', username)
	req.add_header('X-LLNW-Security-Timestamp', timestamp)
	req.add_header('X-LLNW-Security-Token', token)
	response = urllib2.urlopen(req)
	return response
