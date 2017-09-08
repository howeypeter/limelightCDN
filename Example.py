#!/usr/bin/python

import sys
sys.path.append('./limelightCDN')
import limelightCDN
import ConfigParser
import os
import urllib2

profile='default'

urL = "https://api.lldns.net/cfapi/v1/svcinst/delivery/manual/shortname/shutterfly"
query = ""

def read_conf(profile):
  config = ConfigParser.RawConfigParser()
  config.read([os.path.expanduser('~/.llnw/credentials')])
  username = config.get(profile, 'username')
  apikey = config.get(profile, 'apikey')
  return username,apikey

userName,apiKey = read_conf(profile)

#make request
usageReport = limelightCDN.Auth(apiKey)
response = usageReport.GET(urL,userName,queryParameters=query)
print response.read()
