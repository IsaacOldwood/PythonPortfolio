import json

#Load in data
with open(f'RLEsports/TeamMapData.json','r') as f:
    data=json.load(f)

newData={}
mapNames=['Mannfield', 'Champions Field', 'DFH Stadium', 'Wasteland', 'Utopia Coliseum', 'Neo Tokyo', 'Urban Central', 'Forbidden Temple', 'Utopia Colosseum', 'Aquadome', 'Salty Shores', 'Starbase ARC']
big_six=['Renault Vitality', 'Dignitas', 'mousesports', 'G2 Esports', 'NRG Esports', 'Spacestation Gaming']


for mapName in mapNames:
    newData[mapName]={}
    for team in big_six:
        try:
            total=data[team][mapName]['total']
        except KeyError:
            continue

        wins=data[team][mapName]['wins']
        win_rate= wins / total *100

        newData[mapName][team]=round(win_rate)



print(newData)

with open(f'RLEsports/FormattedTeamMapData.json','w') as f:
    json.dump(newData,f,indent=2)