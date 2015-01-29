import os.path
import sys, json


class MailChimpConfig:
    def __init__(self):
        if os.path.isfile('../APIKEY') == False:
            print "Please enter your API Key into the APIKEY file as mentioned in README.md"
            sys.exit()

        f = open('../APIKEY', 'r+')
        apikey = f.read().strip()
        f.close()

        parts = apikey.split('-')
        if len(parts) != 2:
            print "This doesn't look like an API Key: " + apikey
            print "The API Key should have both a key and a server name, separated by a dash, like this: abcdefg8abcdefg6abcdefg4-us1"
            sys.exit()

        self.apikey   = parts[0]
        self.shard    = parts[1]
        self.api_root = "https://" + self.shard + ".api.mailchimp.com/3.0"


def CallOutput(response):
    print response.url
    print "Response Code: " + str(response.status_code) + " " + response.reason
    print "Headers:"
    for header in response.headers:
        print '\t'.join(['',header.ljust(20), response.headers[header]])

    print "\nJSON:"
    print json.dumps(response.json(), indent=4, sort_keys=True)
