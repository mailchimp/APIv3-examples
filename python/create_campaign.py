# This example shows a basic POST request to create a new campaign
# See below, there are several variables you need to update

import requests # Need to install
import json
from config import MailChimpConfig

config = MailChimpConfig()

path = "campaigns"
endpoint = config.api_root + path

# Create metadata for campaign
# See: http://developer.mailchimp.com/documentation/mailchimp/reference/campaigns/
meta = {}

meta['recipients'] = {
    # Insert recipient list ID here
    # See: Lists > Settings > List name and campaign defaults for ID
    'list_id': 'ABCDE12345'
}

meta['settings'] = {
    'subject_line': 'New product announcement!', # Subject line 
    'from_name': 'Your company', # From name
    'title': '1/1/16: New product', # Campaign title
    'inline_css': True, # Automatically inline CSS
    'fb_comments': False, # Facebook comments
    'auto_footer': False, # Auto MailChimp footer
    'to_name': '*|FNAME|* *|LNAME|*', # To name (See merge tag cheat sheet: http://kb.mailchimp.com/merge-tags/all-the-merge-tags-cheat-sheet)
    'folder_id': '', # Put campaign in folder
    'reply_to': 'test@test.com', # Reply-to email
    'auto_tweet': False, # Auto tweet newsletter
}

meta['type'] = 'regular' # Campaign type

#print meta

# JSON-ify metadata
payload = json.dumps(meta)

#print payload

# Send  post request
response = requests.post(endpoint, auth=('apikey', config.apikey), data=payload)

#print response.json()

try:
    response.raise_for_status()
    body = response.json()
    id = body['id']
    # Print out new campaign ID to do something else with it (like set content)
    print id
except requests.exceptions.HTTPError as err:
    print '\n\n\nError: %s' % err