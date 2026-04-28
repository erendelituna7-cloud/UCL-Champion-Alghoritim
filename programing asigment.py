#Import to pandas to  read csv
import pandas as pd

# Make data equal to the data 
data = pd.read_csv("ucl.csv")

# Open new variable to store the team stats 
team_stats = []

# Build a sorted list of every unique team that appears as either home or away
all_teams = sorted(set(data["homeTeam"].tolist() + data["awayTeam"].tolist()))

# Apply this functions to each team 
for team in all_teams:

    # Check how much each team play in thier home stadium 
    home = data[data["homeTeam"] == team]

    # Check how much each team play in the away stadium 
    away = data[data["awayTeam"] == team]
    
    # Check how much each team play  total match
    total_matches = len(home) + len(away)

    # Add the home wins and aways wins to get a total wins for each team 
    wins = len(home[home["FTR"] == "H"]) + len(away[away["FTR"] == "A"])

    # Add the home draws and aways draws to get a total wins for each team 
    draws = len(home[home["FTR"] == "D"]) + len(away[away["FTR"] == "D"])

    # Add the home goals and aways goals to get a total wins for each team
    goals_scored = home["FTHG"].sum() + away["FTAG"].sum()

    # Add the home goals conceded and aways  goals conceded to get a total wins for each team
    goals_conceded = home["FTAG"].sum() + away["FTHG"].sum()

    # To calculate to total points for each team add total win and total draw, write three points per win and one point for per draw
    points = (wins * 3) + draws

    # Store this team's stats as a dictionary and add it to the list
    team_stats.append({
        "Team":   team,
        "Wins":   wins,
        "GF":     goals_scored,
        "GA":     goals_conceded,
        "GD":     goals_scored - goals_conceded,
        "Points": points,
        "draws" : draws,
        "home": home,
        "away": away,
    })

# Convert the list of team dictionaries into a Pandas DataFrame for easy sorting
table = pd.DataFrame(team_stats)

# Copmare the teams with Points, Goal Differsance, and Goals for 
table = table.sort_values(["Points", "GD", "GF"], ascending=False)

# Reset index so rankings are clean numbers nstead of leftover original positions
table = table.reset_index(drop=True)

# Shift index to start at 1 so position 1 = 1st place, matching how rankings are normally read
table.index = table.index + 1  

# Display to top 5 teams get to teams in the table until index 5
top5 = table.head(5) 

# Print UCL 2025/26 PREDICTED WINNER for output
print("  UCL 2025/26 PREDICTED WINNER")

# Print team in the first index in the table for output
print(f"  CHAMPION: {table.loc[1, 'Team']} ")

# Print TOP 5 RANKING: for output
print("  TOP 5 RANKING:")

# Print each of the top 5 teams in a formatted row with their key stats
for rank in range(1, 6):
    row = top5.loc[rank]
    print(f"  #{rank} {row['Team']:<20} {row['Points']} pts  GD: {row['GD']} W:{row['Wins']} GF:{row['GF']} GA:{row['GA']}")
