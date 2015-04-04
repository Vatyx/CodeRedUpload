import sys
import clearbit

clearbit.key = '7ede27940236a369682ac4e7f411da85'
url = sys.argv[1]

company = clearbit.Company.find(domain=url, stream=True)
if company != None:
  print json.dumps(company).encode("UTF-8")
