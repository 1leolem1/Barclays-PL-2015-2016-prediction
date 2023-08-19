import requests as r
import pandas as pd

API_KEY = '9d27c091e43d4110b0d905be9bb3c2b6'
headers = {'X-Auth-Token': API_KEY}
l1_url = 'https://api.football-data.org/v2/competitions/2015/matches'

response = r.get(l1_url, headers=headers)
data = response.json()
matches = pd.DataFrame(data["matches"])

# Step 1: Find the Latest Season
season_ids = [match["season"]["id"] for match in data["matches"]]
latest_season_id = max(season_ids)

# Step 2: Filter the Matches for the Latest Season
latest_season_matches = matches[matches['season'].apply(
    lambda x: x['id']) == latest_season_id]

home_list = []
away_list = []

# Iterate through filtered matches
for index, match in latest_season_matches.iterrows():
    finished = match["status"] == "FINISHED"
    if finished:
        home = match["score"]["fullTime"]["homeTeam"]
        away = match["score"]["fullTime"]["awayTeam"]
        print(f"{home} - {away}")
        home_list.append(home)
        away_list.append(away)
