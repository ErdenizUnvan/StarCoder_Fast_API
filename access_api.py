import requests
import json
hf_apikey='Your HUGGING FACE API KEY'

url = "http://127.0.0.1:8000/generate"
headers = {"Content-Type": "application/json","Authorization": f"Bearer {hf_apikey}"}
query=input('Type your request: ')
payload = {"prompt": query}
response = requests.post(url, headers=headers, data=json.dumps(payload))
print(response.json())
