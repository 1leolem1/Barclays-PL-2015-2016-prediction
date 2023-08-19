import requests as r
import matplotlib.pyplot as plt
import pandas as pd

API_KEY = '9d27c091e43d4110b0d905be9bb3c2b6'
headers = {'X-Auth-Token': API_KEY}
url = 'https://api.football-data.org/v2/competitions/'

response = r.get(url, headers=headers)
data = response.json()

print(str(data))
