import requests

import json
with open(r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Google Drive\Python\shopTitans\prices\components\glowShroom.json') as f:
            payload=json.load(f)

headers1={
    "content-Type":"application/json; charset=utf-8",
    "dataType":"json",
}

#payload='{"key":"value"}'

r=requests.post('https://jsonstorage.net/api/items/',headers=headers1,data=str(payload))
print(r.text)