#!/usr/bin/python

import sys
sys.path.append('./limelightCDN')
import limelightCDN
import ConfigParser
import os
import urllib2

profile='phowey1'

urL = "https://control.llnw.com/traffic-reporting-api/v2/usage"
query = "shortname=shutterfly&service=http&service=https&endDate=2017-09-02&startDate=2017-09-01&reportDuration=custom"

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
