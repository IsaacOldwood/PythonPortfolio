import requests
import json
import pickle

#api.octane.gg

big_six=['Renault Vitality', 'Dignitas', 'mousesports', 'G2 Esports', 'NRG Esports', 'Spacestation Gaming']

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
    #Collects all played match URLs

    r=requests.get('https://api.octane.gg/api/matches?page=1')
    json=r.json()

    last_page=json['last_page']

    jsonData=json['data']

    all_match_urls=[jsonData[i]['match_url'] for i in range(0,20)]

    for pageNo in range(1,(last_page+1)):
        r=requests.get(f'https://api.octane.gg/api/matches?page={pageNo}')
        json=r.json()

        jsonData=json['data']

        match_urls=[jsonData[i]['match_url'] for i in range(0,len(jsonData))]
        all_match_urls.extend(match_urls)

        #Save every 20 pages
        if pageNo % 20==0:
            with open('RLEsports/all_match_urls.txt', 'wb') as f:
                pickle.dump(all_match_urls, f)
            
            print(f'Page {pageNo} complete')

    with open('RLEsports/all_match_urls.txt', 'wb') as f:
                pickle.dump(all_match_urls, f)

    print('Successfully collected and saved all macth URLs')

def readAllMatchUrls():

    with open ('RLEsports/all_match_urls.txt', 'rb') as f:
        all_match_urls = pickle.load(f)

    return all_match_urls
    
def collectSeriesData(match_url):
    #https://api.octane.gg/api/match/MATCHID or https://api.octane.gg/api/series/MATCHID 

    r=requests.get(f'https://api.octane.gg/api/series/{match_url}')
    JSON=r.json()

    return JSON

def collectGameData(match_url,game_no):
    #https://api.octane.gg/api/match_scoreboard_info/4770126/1

    r=requests.get(f'https://api.octane.gg/api/match_scoreboard_info/{match_url}/{game_no}')
    JSON=r.json()

    return JSON

def collectMatchURLIncludingTeams(team_list,list_name):
    
    all_match_url=readAllMatchUrls()
    saved_URLs=[]
    counter=0

    for match_url in all_match_url:
        counter+=1
        JSON=collectSeriesData(match_url)
        try:
            team1=JSON['data'][0]['Team1']
            team2=JSON['data'][0]['Team2']
        except KeyError:
            print(f'Failed on {match_url}')
            break

        if (team1 in team_list) or (team2 in team_list):
            saved_URLs.append(match_url)

        if counter % 25==0:
            with open(f'RLEsports/{list_name}URLs.txt', 'wb') as f:
                pickle.dump(saved_URLs, f)
            print(f'{counter} matches checked')

    with open(f'RLEsports/{list_name}URLs.txt', 'wb') as f:
            pickle.dump(saved_URLs, f)

    print('Successfully collected all match URLs for given teams')    

def readTeamURLs(list_name):

    with open(f'RLEsports/{list_name}URLs.txt', 'rb') as f:
        savedURLs=pickle.load(f)

    return savedURLs

def collectTeamMapInfo(match_urls,team_list):
    collectedData={}

    for team in team_list:
        teamData={}
        collectedData[team]=teamData

    for matchURL in match_urls:
        JSON=collectSeriesData(matchURL)
        total_games=JSON['data'][0]['Team1Games'] + JSON['data'][0]['Team2Games']

        for i in range(1,total_games+1):
            #Collect data
            gameData=collectGameData(matchURL,i)
            try:
                mapName=gameData['data']['Map']
                team1=gameData['data']['Team1']
                team2=gameData['data']['Team2']
                result=gameData['data']['Result']
            except KeyError:
                print(f'No game data found for match: {matchURL}, game: {i}. Moving onto next match...')
                break

            #Add to dictionary
            if team1 in team_list:
                if mapName not in collectedData[team1]:
                    collectedData[team1][mapName]= {
                        "total": 0,
                        "wins": 0
                    }
                
                if result == team1:
                    collectedData[team1][mapName]['wins']+=1
                
                collectedData[team1][mapName]['total']+=1

            if team2 in team_list:
                if mapName not in collectedData[team2]:
                    collectedData[team2][mapName]= {
                        "total": 0,
                        "wins": 0
                    }

                if result == team2:
                    collectedData[team2][mapName]['wins']+=1
                
                collectedData[team2][mapName]['total']+=1


    #Save collected Data
    with open(f'RLEsports/TeamMapData.json','w') as f:
        json.dump(collectedData,f,indent=2)

    return collectedData

savedURLs=readTeamURLs('bigSix')

collectedData=collectTeamMapInfo(savedURLs,big_six)

print(collectedData)

