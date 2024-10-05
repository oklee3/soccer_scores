from stats import *
import json
import requests

api_key = 'fa7bb5fd5de8461fb040abdb404b651a'
headers = {'X-Auth-Token': api_key}

base_url = "https://api.football-data.org/v4/competitions/"
league_ids = ["PL", "SA", "PD", "BL1", "FL1"] 

try:
    with open("team_crests.json", "r") as f:
        team_crests = json.load(f)
except FileNotFoundError:
    team_crests = {}

for league_id in league_ids:
    # endpoint for each league
    endpoint = f"{base_url}{league_id}/teams"
    
    response = requests.get(endpoint, headers=headers)
    
    if response.status_code == 200:
        teams_data = response.json()
        
        # add/update crests in the dictionary
        for team in teams_data['teams']:
            team_name = team['name']
            crest_url = team['crest']
            team_crests[team_name] = crest_url
    else:
        print(f"Failed to fetch data for league ID: {league_id}. Status code: {response.status_code}")

# save the updated dictionary back to the JSON file
with open("team_crests.json", "w") as f:
    json.dump(team_crests, f)

print("Crest URLs updated successfully for all specified leagues!")
