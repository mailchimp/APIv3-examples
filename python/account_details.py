# This request returns basic account details from the API and verifies that the key is valid
from config import MailChimpConfig, CallOutput
import requests, json

config = MailChimpConfig()

headers  = {'Authorization': 'apikey ' + config.apikey}       # Authentication is done via request header in version 3.0
endpoint = config.api_root + "/"

response = requests.get(endpoint, headers=headers)

CallOutput(response)
