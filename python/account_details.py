# This example shows a basic GET request that returns all data.

import requests
import json
from config import MailChimpConfig

config = MailChimpConfig()

endpoint = config.api_root

response = requests.get(endpoint, auth=('apikey', config.apikey))
print response.url

try:
  response.raise_for_status()
  response_json = response.json()
except requests.exceptions.HTTPError as err:
  print 'Error: %s' % err
except ValueError:
  print "Cannot decode JSON, got %s" % response.text

print "Headers:"
for header in response.headers:
    print '\t'.join(['',header.ljust(20), response.headers[header]])

print "\nJSON:"
print json.dumps(response_json, indent=4)
