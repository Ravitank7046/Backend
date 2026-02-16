import requests
import json

URL = 'http://localhost:8000/st/'

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    res = requests.get(url=URL,data=json_data)
    data = res.json()
    print(data)

# get_data(2)    


def post_data():
    data = {'name':'Harshil Kalavadiya','roll':102,'city':'Banaras'}
    json_data = json.dumps(data)
    res = requests.post(url=URL,data=json_data)
    data = res.json()
    print(data)

post_data()
