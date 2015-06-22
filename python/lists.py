""" This example demonstrates showing some basic details about your lists
Below you can see examples of pagination as well as partial response
"""

import requests
import json
try:
    import urlparse
except ImportError:
    from urllib import parse as urlparse
from config import MailChimpConfig


config = MailChimpConfig()

endpoint = urlparse.urljoin(config.api_root, 'lists')
params = {
    # With Partial Response, you choose which fields you want to see
    'fields': 'lists.id,lists.name,lists.stats.member_count',
    # Pagination in API v3.0 is always done with count and offset
    'count': 10, 'offset': 0
}

total_lists = 0

while True:
    response = requests.get(endpoint, auth=('apikey', config.apikey),
                            params=params, verify=False)

    try:
      response.raise_for_status()
      body = response.json()
    except requests.exceptions.HTTPError as err:
        print "Error: {} {}".format(str(response.status_code), err)
        print json.dumps(response.json(), indent=4)
        break
    except ValueError:
        print "Cannot decode json, got %s" % response.text
        break

    if len(body['lists']) == 0:
        break

    total_lists += len(body['lists'])

    for user_list in body['lists']:
        print u'%s: %s (Subscribers: %s)' % (
            user_list['id'],
            user_list['name'],
            user_list['stats']['member_count'])

    params['offset'] += params['count']

print "\n" + str(total_lists) + " lists found."
