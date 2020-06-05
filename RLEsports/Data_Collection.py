import requests
import json

#api.octane.gg

def collectAllTeams():
    
    r=requests.get('https://api.octane.gg/api/search/teams/')
    json=r.json()
    return json

def collectAllPlayers():
    
    r=requests.get('https://api.octane.gg/api/search/players/')
    json=r.json()
    return json

def collectAllEvents():
    
    r=requests.get('https://api.octane.gg/api/search/events')
    json=r.json()
    return json

