#!/usr/bin/python
import sys
import cgi, cgitb
import urllib
import urllib2
import json
keyBing="rUX6u17MhAbZ7jn7GmRKkucXRlh5ZxGqLWkZShIpbxY"
credentialBing = 'Basic ' + (':%s' % keyBing).encode('base64')[:]
#searchString= cgi.FieldStorage()
searchString = '%27Xbox+One%27'
top = 20
offset = 0
url = 'https://api.datamarket.azure.com/Bing/Search/News?' + \
      'Query=%s&$top=%d&$skip=%d&$format=json' % (searchString, top, offset)
request = urllib2.Request(url)
request.add_header('Authorization', credentialBing)
requestOpener = urllib2.build_opener()
response = requestOpener.open(request) 
results = json.load(response)
print "Content-Type: text/html\n"
print results
