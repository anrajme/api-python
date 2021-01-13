import requests
req_data=requests.get("http://api.open-notify.org/iss-now.json")

json_data=req_data.json()

print('\t'.join(list(json_data['iss_position'].keys())))
print('\t'.join(list(json_data['iss_position'].values())))
