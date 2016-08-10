#
#            !!! DANGER !!!
#            !!! DANGER !!!
#            !!! DANGER !!!
#
# This script will send an email to all recipients of campaign
# To test the email, use the test_email.py file

import requests
import json
from config import MailChimpConfig, GetCampaignID

config = MailChimpConfig()
campaign_id = GetCampaignID()

email = "campaigns/{0}/actions/send".format(campaign_id)
endpoint = config.api_root + email

response = requests.post(endpoint, auth=('apikey', config.apikey))

#print "\nURL: " + response.url + "\n\n"

try:
    response.raise_for_status()
    print "\n\nSENT!!!\n\n"
except requests.exceptions.HTTPError as err:
    print '\n\n\nError: %s' % err

print "\nHeaders:"
for header in response.headers:
    print '\t'.join(['',header.ljust(20), response.headers[header]])
