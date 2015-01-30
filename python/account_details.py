# This example shows a basic GET request that returns all data.

from config import MailChimpConfig
import requests, json

config = MailChimpConfig()

headers  = {'Authorization': 'apikey ' + config.apikey}       # Authentication is done via request header in version 3.0
endpoint = config.api_root + "/"

response = requests.get(endpoint, headers=headers)

print response.url
print 'Error: {} {}'.format(str(response.status_code), response.reason)
print "Headers:"
for header in response.headers:
    print '\t'.join(['',header.ljust(20), response.headers[header]])

print "\nJSON:"
print json.dumps(response.json(), indent=4)
