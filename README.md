# UCL 25/26 Winner Prediction 
Simple phyton project that can help to predict to which teamwill win the champions Leuge 

#  What It Does
Reads match results from a CSV file and calculates each team's:
- **Wins** and **Draws**
- **Goals For (GF)** and **Goals Against (GA)**
- **Goal Difference (GD)**
- **Total Points** (3 per win, 1 per draw)

It then ranks all teams and prints the **Top 5**, declaring the team at the top as the predicted champion.

## Requirements
- Python 3.7
- pip install pandas
[pandas](https://pandas.pydata.org/)

##  Usage
Script can be simply run in the terminal

##  Notes

- Rankings are sorted by **Points** first, then **Goal Difference** as a tiebreaker.
- This is a stats-based prediction using existing match data

## Bug
-  Sprict has conatin a one bug that , even thoug bayern and arsenel share the same goal code becuse of pyhton raking by Alphabetic line Arsenal coming before Bayern. That reoson script put Areseanl before Bayern.

##  License

Free to use and modify. Have fun!
