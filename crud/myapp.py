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

# get_data()    


def post_data():
    data = {'name':'Sohit','roll':110,'city':'surat'}
    json_data = json.dumps(data)
    res = requests.post(url=URL,data=json_data)
    data = res.json()
    print(data)

post_data()

def update_data():
    data = {
        'id':'6',
        'name':"Mehul Tank",
    }
    json_data = json.dumps(data)
    res = requests.put(url=URL,data=json_data)
    data = res.json()
    print(data)

# update_data()

def delete_data():
    data = {'id':'6'}
    json_data = json.dumps(data)
    res = requests.delete(url=URL,data=json_data)
    data = res.json()
    print(data)

# delete_data()
