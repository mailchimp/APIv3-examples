# This example shows a basic POST request that sends a test email.

import requests # Need to install
import json
from config import MailChimpConfig

config = MailChimpConfig()

# Set your variables here
campaign_id = "ABCD1234" # INSERT CAMPAIGN ID HERE
test_email = ["test@test.com"] # INSERT TEST EMAIL HERE

test = "campaigns/{0}/actions/test".format(campaign_id)
endpoint = config.api_root + test

payload = json.dumps({"test_emails": test_email, "send_type": "html"})

#print  "\nPayload: " + payload

response = requests.post(endpoint, auth=('apikey', config.apikey), data=payload)

#print "\nURL: " + response.url + "\n\n"

try:
    response.raise_for_status()
    print "\n\n Test sent \n\n"
except requests.exceptions.HTTPError as err:
    print '\n\n\nError: %s' % err
