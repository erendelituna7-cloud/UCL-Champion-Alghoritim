import pandas as pd

data = pd.read_csv("ucl.csv")

team_stats = []

all_teams = sorted(set(data["homeTeam"].tolist() + data["awayTeam"].tolist()))

for team in all_teams:

    home = data[data["homeTeam"] == team]

    away = data[data["awayTeam"] == team]

    total_matches = len(home) + len(away)

    wins = len(home[home["FTR"] == "H"]) + len(away[away["FTR"] == "A"])
   
    draws = len(home[home["FTR"] == "D"]) + len(away[away["FTR"] == "D"])

    goals_scored = home["FTHG"].sum() + away["FTAG"].sum()

    goals_conceded = home["FTAG"].sum() + away["FTHG"].sum()

    points = (wins * 3) + draws

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

table = pd.DataFrame(team_stats)

table = table.sort_values(["Points", "GD"], ascending=False)
table = table.reset_index(drop=True)
table.index = table.index + 1  

top5 = table.head(5)

print("  UCL 2025/26 PREDICTED WINNER")

print(f"  CHAMPION: {table.loc[1, 'Team']} ")
print("  TOP 5 RANKING:")
for rank in range(1, 6):
    row = top5.loc[rank]
    print(f"  #{rank} {row['Team']:<20} {row['Points']} pts  GD: {row['GD']} W:{row['Wins']} GF:{row['GF']} GA:{row['GA']}")