#!/usr/local/bin/python3
import requests
request = requests.get('http://api.open-notify.org/astros.json')
req_json=request.json()
print("Total numbe of Austronauts: ", req_json['number'])
for i in req_json['people']:
	print(i['name'])

