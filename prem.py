import requests

# Replace with your own API key
API_KEY = 'YOUR_API_KEY'

# Headers for authentication
headers = {'X-Auth-Token': API_KEY}

def get_current_matchday(headers):
    """
    Fetches the current matchday for the Premier League
    """
    url = 'https://api.football-data.org/v4/competitions/PL'
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        current_matchday = data['currentSeason']['currentMatchday']
        return current_matchday

def get_latest_premier_league_scores(headers):
    """
    Function that generates scores from the most recent PL matchweek.
    When a new matchweek begins, the batch of scores is updated.
    """
    current_matchday = get_current_matchday(headers)

    url = f'https://api.football-data.org/v4/competitions/PL/matches?matchday={current_matchday}'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        if not data['matches']:
            print(f"No matches found for Matchday {current_matchday}.")  # If no matches found
            return

        for match in data['matches']:
            home_team = match['homeTeam']['name']
            away_team = match['awayTeam']['name']
            home_score = match['score']['fullTime']['home']
            away_score = match['score']['fullTime']['away']
            match_date = match['utcDate']

            print(f"{match_date}: {home_team} {home_score} - {away_score} {away_team}")

def get_table(headers):
    """
    Function that prints the current PL table
    """
    url = 'https://api.football-data.org/v4/competitions/PL/standings'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        for team in data['standings']:
            print(team)