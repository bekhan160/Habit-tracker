
import requests
import json

data = {'habit': 'gym'}
headers = {'Content-type': 'application/json'}
response = requests.post('http://127.0.0.1:8000/habit', data=json.dumps(data), headers=headers)

print(response.status_code)
print(response.json())
