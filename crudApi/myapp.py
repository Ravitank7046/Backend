import requests
import json

URL = 'http://localhost:8000/studentApi/'

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    res = requests.get(url=URL,headers=headers,data=json_data)
    data = res.json()
    print(data)
# get_data()    


def post_data():
    data = {'name':'Salman Khan','city':'Mumbai','aadharNumber':124578895623,'schoolName':"Tapovan School"}
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    res = requests.post(url=URL,headers=headers,data=json_data)
    data = res.json()
    print(data)

# post_data()

def update_data(id):
    data = {'id':id,'name':'Ajay Modi','city':'surat','aadharCardNumber':754512457112,'schoolName':"Jain Univercity"}
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    res = requests.put(url=URL,headers=headers,data=json_data)
    data = res.json()
    print(data)

# update_data(2)

def delete_data(id):
    data = {'id':id}
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    res = requests.delete(url=URL,headers=headers,data=json_data)
    data = res.json()
    print(data)

delete_data(1)
