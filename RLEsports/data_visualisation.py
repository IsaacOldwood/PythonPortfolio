import json
import matplotlib as plt

#Load in data
with open(f'RLEsports/TeamMapData.json','r') as f:
    data=json.load(f)

print(data)