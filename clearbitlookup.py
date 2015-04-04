#!/usr/bin/python
import sys
import clearbit
import cgi, cgitb
import json
#cgitb.enable()
clearbit.key = '7ede27940236a369682ac4e7f411da85'
url = cgi.FieldStorage()
#url ="www.intel.com"
print "Content-Type: text/html\n"

company = clearbit.Company.find(domain=url["ourwebsite"].value, stream=True)
if company != None:
  print json.dumps(company).encode("UTF-8")
