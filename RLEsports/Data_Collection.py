import requests
import json
import pickle

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

def collectMatchUrls():
    #https://api.octane.gg/api/matches?page=2  20 per page

    r=requests.get('https://api.octane.gg/api/matches?page=1')
    json=r.json()

    last_page=json['last_page']

    jsonData=json['data']

    all_match_urls=[jsonData[i]['match_url'] for i in range(0,20)]

    for pageNo in range(1,(last_page+1)):
        r=requests.get(f'https://api.octane.gg/api/matches?page={pageNo}')
        json=r.json()

        jsonData=json['data']

        match_urls=[jsonData[i]['match_url'] for i in range(0,20)]
        all_match_urls.append(match_urls)

    with open('RLEsports/all_match_urls.txt', 'wb') as f:
        pickle.dump(all_match_urls, f)

    print('Successfully collected and saved all macth URLs')

def readAllMatchUrls():

    with open ('RLEsports/all_match_urls.txt', 'rb') as f:
        all_match_urls = pickle.load(f)

    return all_match_urls
    

    

all_match_urls=readAllMatchUrls()

print(len(all_match_urls))

