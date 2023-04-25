
import requests
import json

data = {'habit_name': 'walk', 'descriptions': 'walking', 'target': 5, 'frequency': 2}
headers = {'Content-type': 'application/json'}
response = requests.post('http://127.0.0.1:8000/api/user/', data=json.dumps(data), headers=headers)

print(response.status_code)
print(response.json())
