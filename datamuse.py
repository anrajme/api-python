#!/usr/local/bin/python3
import requests
parameter={"rel_rhy":"jingle"}
request=requests.get('https://api.datamuse.com/words',parameter)
req_json=request.json()
print(req_json)
