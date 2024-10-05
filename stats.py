import requests

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
    Function that returns the scores from the most recent league matchweek.
    When a new matchweek begins, the batch of scores is updated.
    Returns a list containing each team as a dictionary.
    """
    current_matchday = get_current_matchday(headers, league_ID)
    url = f'https://api.football-data.org/v4/competitions/{league_ID}/matches?matchday={current_matchday}'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        if not data['matches']:
            return f"No matches found for Matchday {current_matchday}."  # Return a message if no matches found

        scores = []

        for match in data['matches']:
            match_info = {
                'Date': match['utcDate'],
                'Home Team': match['homeTeam']['name'],
                'Away Team': match['awayTeam']['name'],
                'Home Score': match['score']['fullTime']['home'],
                'Away Score': match['score']['fullTime']['away']
            }
            scores.append(match_info)

        return scores
    else:
        return None

def get_table(headers, league_ID):
    """
    Function that returns the current league table as a list of dictionaries.
    """
    url = f'https://api.football-data.org/v4/competitions/{league_ID}/standings'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        table = []

        for standing in data['standings']:
            for team in standing['table']:
                team_info = {
                    'Pos': team['position'],
                    'Club': team['team']['name'],
                    'Crest': team['team']['crest'],
                    'MP': team['playedGames'],
                    'W': team['won'],
                    'D': team['draw'],
                    'L': team['lost'],
                    'Pts': team['points'],
                    'GD': team['goalDifference']
                }
                table.append(team_info)

        return table
    else:
        return None
