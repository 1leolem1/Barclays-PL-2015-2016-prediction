from statsbombpy import sb
import pandas as pd
from mplsoccer import VerticalPitch, Pitch
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import seaborn as sns

season_id = 27
comp = "Premier League"

free_comps = sb.competitions()
season = free_comps[(free_comps["competition_name"] == "Premier League") & (
    free_comps["season_id"] == season_id)]

print(season)
