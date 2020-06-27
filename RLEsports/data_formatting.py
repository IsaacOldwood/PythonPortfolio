import json

#Load in data
with open(f'RLEsports/TeamMapData.json','r') as f:
    data=json.load(f)

newData={}
mapNames=["Mannfield","Champions Field","DFH Stadium","Wasteland","Utopia Coliseum","Neo Tokyo","Urban Central","Forbidden Temple","Utopia Colosseum","Aquadome"]

for team in data:
    data[team]
    for mapName in data[team].keys():
        if mapName not in mapNames:
            mapNames.append(mapName)

print(mapNames)