import requests
import json

URL = 'http://127.0.0.1:8000/'

data = {
    'name':'Ravi',
    'roll':101,
    'city':'Surat'
}
json_data = json.dumps(data)
r = requests.post(url=URL,data=data)