import json
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

#Load in data
with open(f'RLEsports/TeamMapData.json','r') as f:
    data=json.load(f)

big_six=['Renault Vitality', 'Dignitas', 'mousesports', 'G2 Esports', 'NRG Esports', 'Spacestation Gaming']
team_win_rates=[]
mapName='Mannfield'
for team in big_six:
    team_win_rate=data[team][mapName]['wins'] / data[team][mapName]['total'] *100
    team_win_rates.append( round(team_win_rate) )

fig = plt.figure()
ax = plt.axes(projection="3d")

num_bars = 6
x_pos = [0,0,2,2,4,4]
y_pos = [0,2,0,2,0,2]
z_pos = [0] * num_bars
x_size = np.ones(num_bars)
y_size = np.ones(num_bars)
z_size = team_win_rates

ax.bar3d(x_pos, y_pos, z_pos, x_size, y_size, z_size, color=('black','yellow','red','grey','blue','purple'))
fig.suptitle(mapName)
plt.axis('off')
ax.view_init(elev=50, azim=-80)
ax.text(0.5,0.5,team_win_rates[0],f'RV\n{team_win_rates[0]}%',ha='center',va='center',color='white')
ax.text(0.5,2.5,team_win_rates[1],f'DIG\n{team_win_rates[1]}%',ha='center',va='center',color='white')
ax.text(2.5,0.5,team_win_rates[2],f'MOUZ\n{team_win_rates[2]}%',ha='center',va='center',color='white')
ax.text(2.5,2.5,team_win_rates[3],f'G2\n{team_win_rates[3]}%',ha='center',va='center',color='white')
ax.text(4.5,0.5,team_win_rates[4],f'NRG\n{team_win_rates[4]}%',ha='center',va='center',color='white')
ax.text(4.5,2.5,team_win_rates[5],f'SSG\n{team_win_rates[5]}%',ha='center',va='center',color='white')
plt.show()