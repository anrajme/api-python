#!/usr/local/bin/python3
OAUTH_TOKEN="ya29.a0AfH6SMB8fyE22zH9hLm41mHQ8KOHwRkKeJ_fdZGbpwNXLRXjRjV9fHIlCYeIoLqq3F0316NT-_lOKFePpyLX813kBdERAUej_PWQJvC3nhHfrTVg8JPZoJIXDPWBRUmDXYxdGnEyLcBss5f32nEuYQyoCsEb3hgHci8"
import requests
import json
url = "https://www.googleapis.com/fitness/v1/users/me/dataSources"

headers = { 'content-type': 'application/json',
            'Authorization': 'Bearer %s' % OAUTH_TOKEN }
r = requests.get(url, headers=headers).text
data = json.loads(r)

print (data)
