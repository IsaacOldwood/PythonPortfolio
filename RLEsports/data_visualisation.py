import json

#Load in data
with open(f'RLEsports/TeamMapData.json','r') as f:
    data=json.load(f)

print(data)