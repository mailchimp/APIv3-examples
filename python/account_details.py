# This example shows a basic GET request that returns all data.

from config import MailChimpConfig
import requests, json

config = MailChimpConfig()

endpoint = config.api_root + "/"

response = requests.get(endpoint, auth=('apikey', config.apikey))

print response.url
print 'Error: {} {}'.format(str(response.status_code), response.reason)
print "Headers:"
for header in response.headers:
    print '\t'.join(['',header.ljust(20), response.headers[header]])

print "\nJSON:"
print json.dumps(response.json(), indent=4)
