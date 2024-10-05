import requests

# Replace with your own API key
API_KEY = 'YOUR_API_KEY'

# Headers for authentication
headers = {'X-Auth-Token': API_KEY}

def get_current_matchday(headers, league_ID):
    """
    Fetches the current matchday for the given league
    """
    url = f'https://api.football-data.org/v4/competitions/{league_ID}'
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        current_matchday = data['currentSeason']['currentMatchday']
        return current_matchday

def get_latest_league_scores(headers, league_ID):
    """
    Function that generates scores from the most recent league matchweek.
    When a new matchweek begins, the batch of scores is updated.
    """
    current_matchday = get_current_matchday(headers, league_ID)

    url = f'https://api.football-data.org/v4/competitions/{league_ID}/matches?matchday={current_matchday}'

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

def get_table(headers, league_ID):
    """
    Function that prints the current league table
    """
    url = f'https://api.football-data.org/v4/competitions/{league_ID}/standings'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        print(f"{'Position':<10}{'Team':<30}{'Points':<10}{'Wins':<10}{'Draws':<10}{'Losses':<10}{'Goal Difference':<15}")
        print("=" * 95)

        for standing in data['standings']:
            for team in standing['table']:
                pos = team['position']
                name = team['team']['name']
                points = team['points']
                wins = team['won']
                draws = team['draw']
                losses = team['lost']
                goal_diff = team['goalDifference']

                print(f"{pos:<10}{name:<30}{points:<10}{wins:<10}{draws:<10}{losses:<10}{goal_diff:<15}")