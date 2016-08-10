# This example shows a basic POST request that sends a test email.

import requests
import json
from config import MailChimpConfig, GetCampaignID

config = MailChimpConfig()
campaign_id = GetCampaignID()

test = "campaigns/{0}/actions/test".format(campaign_id)
endpoint = config.api_root + test

payload = json.dumps({"test_emails":["robdentonrg@gmail.com"],"send_type":"html"})

print  "\nPayload: " + payload

response = requests.post(endpoint, auth=('apikey', config.apikey), data=payload)

print "\nURL: " + response.url + "\n\n"

try:
    response.raise_for_status()
    print "\n\nSENT!!!\n\n"
except requests.exceptions.HTTPError as err:
    print '\n\n\nError: %s' % err

print "\nHeaders:"
for header in response.headers:
    print '\t'.join(['',header.ljust(20), response.headers[header]])
