from flask import Flask, render_template, json
from stats import *

api_key = 'fa7bb5fd5de8461fb040abdb404b651a'
headers = {'X-Auth-Token': api_key}

app = Flask(__name__)

@app.route("/")
def tables():
    with open("team_crests.json", "r") as f:
        team_crests = json.load(f)

    big_5_tables = []
    big_5_tables.append({'league' : 'Premier League', 'teams' : get_table(headers, 'PL')})
    big_5_tables.append({'league' : 'La Liga', 'teams' : get_table(headers, 'PD')})
    big_5_tables.append({'league' : 'Serie A', 'teams' : get_table(headers, 'SA')})
    big_5_tables.append({'league' : 'Bundesliga', 'teams' : get_table(headers, 'BL1')})
    big_5_tables.append({'league' : 'Ligue 1', 'teams' : get_table(headers, 'FL1')})

    return render_template('tables.html', tables=big_5_tables, team_crests=team_crests)

if __name__ == '__main__':
    app.run(debug=True)
