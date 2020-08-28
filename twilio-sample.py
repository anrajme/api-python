#!/usr/local/bin/python3
from twilio.rest import Client
import requests

account_sid= ''
auth_token=''

client = Client(account_sid, auth_token)
r = requests.get('http://api.open-notify.org/astros.json')
people = r.json()
number_aus=people['number']

Message = 'Hi Fun fact, Number of people in space right now is ' +str(number_aus)

message = client.messages.create(
	to="+918867731006",
	from_="+12057404455",
	body=Message)
print(message.sid) 
