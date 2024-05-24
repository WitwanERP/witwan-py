import requests
import json


res = requests.get('https://app.atvarquitectos.com/api/menu')
response = json.loads(res.text)
print(response)
