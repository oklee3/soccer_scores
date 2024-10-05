import requests

api_key = ' fa7bb5fd5de8461fb040abdb404b651a'
url = 'https://api.football-data.org/v4/competitions/PL/matches'

headers = {'X-Auth-Token': api_key}

# Send a request to the API
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    # Loop through matches and print score data
    for match in data['matches']:
        home_team = match['homeTeam']['name']
        away_team = match['awayTeam']['name']
        score = match['score']
        print(f'{home_team} vs {away_team} - {score["fullTime"]["homeTeam"]}:{score["fullTime"]["awayTeam"]}')
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
