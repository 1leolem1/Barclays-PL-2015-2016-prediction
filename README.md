**_PROJECT IN PROGRESS :))_**


In this project, I want to predict the results of football games using the free data provided by Statsbomb. 

Hudl Statsbomb provides the full 2015-16 Premier League season for free on its API for EDA and academic purposes (I wish I could have a full season of Ligue 1 instead...)

Anyway, the objective here is to go through the data and predict the last 8 matchdays (almost an 80 - 20 split and it makes sense trying to predict chronologically) **FOR A SPECIFIC TEAM**. I dont think I can create a general model before doing a specialized model first. My data may get trained with the playstyle of a particular team.


Features I plan on using (/ recreating using data):


1. (Goals conceeded / game) at home 
2. (Goals scored / game) at home
3. (Goals conceeded / game) away
4. (Goals conceeded / game) away
7. Convertion strength: (Goals scored / game) - (Xg / game)
11. Xg from crosses 
12. Successful dribbles / game
13. Set pieces / game
14. Xg on set pieces / game


6. Home VS Away game
7. Form
9. Ranking (before match starts! Otherwise, its completely useless since it gives a lookahead) -> Can I find some stronger features than in predicting the game results than it's the 1st at home playing the 18th
10. Avg Possession %

9. Goalkeeper 's impact: (Goals conceeded / game) - (Xg conceeded / game)
14. Successful tackles / game
15. Defensive duels won / game
16. Interceptions / game
17. xGoals conceeded / game on set piece
