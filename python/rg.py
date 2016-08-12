#
#            !!! DANGER !!!
#            !!! DANGER !!!
#            !!! DANGER !!!
#
# This script will send an email to all recipients of campaign
# To test the email, use the test_email.py file

import requests
import json
from config import MailChimpConfig

config = MailChimpConfig()
# print campaign_id

def createCampaign(key):
	path = "campaigns"
	endpoint = config.api_root + path
	
	meta = {}
	
	meta['recipients'] = {
		'segment_opts': {
			'conditions': [{
				'field': 'EMAIL',
				'condition_type': 'EmailAddress',
				'value': 'rob.denton',
				'op': 'contains'
			}],
			'match': 'any'
		},
		'list_id': '824c7efd1d'
	}
	
	meta['settings'] = {
		'subject_line': 'RG Daily Digest',
		'from_name': 'The Register-Gard',
		'title': 'Rob API test 1',
		'inline_css': True,
		'fb_comments': False,
		'auto_footer': False,
		'athenticate': True,
		'to_name': '*|FNAME|* *|LNAME|*',
		'folder_id': '',
		'reply_to': 'promotions@registerguard.com',
		'auto_tweet': False,
	}
	
	meta['type'] = 'regular'
	
	#print meta
	
	payload = json.dumps(meta)
	
	#print payload
	
	response = requests.post(endpoint, auth=('apikey', key), data=payload)
	
	#print response.json()
	
	try:
		response.raise_for_status()
		body = response.json()
		id = body['id']
		return id
	except requests.exceptions.HTTPError as err:
		print '\n\n\nError: %s' % err
	
	

def setContent(key, id):
	content = "campaigns/{0}/content".format(id)
	endpoint = config.api_root + content
	
	payload = json.dumps({"url": "http://registerguard.com/csp/cms/rg/pages/newsletters/news.csp"})
	
	response = requests.put(endpoint, auth=('apikey', key), data=payload)
	
	try:
		response.raise_for_status()
	except requests.exceptions.HTTPError as err:
		print '\n\n\nError: %s' % err
		print response.json()

def sendTest(key, id):
	test = "campaigns/{0}/actions/test".format(id)
	endpoint = config.api_root + test
	
	payload = json.dumps({"test_emails":["robdentonrg@gmail.com"],"send_type":"html"})
	
	#print  "\nPayload: " + payload
	
	response = requests.post(endpoint, auth=('apikey', key), data=payload)
	#print response.json()
	
	#print "\nURL: " + response.url + "\n\n"
	
	try:
		response.raise_for_status()
		print "\n\nTEST SENT!!!\n\n"
	except requests.exceptions.HTTPError as err:
		print '\n\n\nError: %s' % err

# Call method
campaign_id = createCampaign(config.apikey)
#campaign_id = "3b97b6caca" # For testing (use last created campaign ID)
print campaign_id
setContent(config.apikey, campaign_id)
sendTest(config.apikey, campaign_id)

# email = "campaigns/{0}/actions/send".format(campaign_id.cid)
# endpoint = config.api_root + email
# 
# response = requests.post(endpoint, auth=('apikey', config.apikey))
# 
# #print "\nURL: " + response.url + "\n\n"
# 
# try:
#     response.raise_for_status()
#     print "\n\nSENT!!!\n\n"
# except requests.exceptions.HTTPError as err:
#     print '\n\n\nError: %s' % err
# 
# print "\nHeaders:"
# for header in response.headers:
#     print '\t'.join(['',header.ljust(20), response.headers[header]])


