import requests
import json

r=requests.get('https://api.octane.gg/api/matches/?sort=&page=1&per_page=100')
json=r.json()

print(json)