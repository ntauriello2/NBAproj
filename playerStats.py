from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
import pandas as pd

playerIDS = {
    "Nikola Jokic": "203999",
    "Luka Doncic": "1629029",
    "LeBron James": "2544",
    "Stephen Curry": "201939",
    "Anthony Davis": "203076",
    "Giannis Antetokounmpo": "203507",
    "Joel Embiid": "203954",
    "Anthony Edwards": "1630162",
    "Shai Gilgeous-Alexander": "1628983",
    "Kevin Durant": "201142",
    "Damian Lillard": "203081",
    "Bam Adebayo": "1628389",
    "Jayson Tatum": "1628369",
    "Jalen Brunson": "1628973",
    "Tyrese Haliburton": "1630169",
    "Paolo Banchero": "1631094",
    "Scottie Barnes": "1630567",
    "Devin Booker": "1626164",
    "Jaylen Brown": "1627759",
    "Paul George": "202331",
    "Tyrese Maxey": "1630178",
    "Donovan Mitchell": "1628378",
    "Kawhi Leonard": "202695",
    "Trae Young": "1629027",
    "Karl-Anthony Towns": "1626157",
    "Julius Randle": "203944",
    "James Harden": "201935",
    "LaMelo Ball": "1630163",
    "DeMar DeRozan": "201942",
    "Zach LaVine": "203897",
    "Jimmy Butler": "202710",
}

plusMinus = {}

# Loop through each player
for name, player_id in playerIDS.items():

    stats = playergamelog.PlayerGameLog(player_id=player_id, season='2023')
    gamelog = stats.get_data_frames()[0]
    
    total_plus_minus = gamelog['PLUS_MINUS'].sum()
       
    plusMinus[name] = total_plus_minus

plusMinus_sorted = dict(sorted(plusMinus.items(), key=lambda item: item[1], reverse=True))


print("MVP based on plus/minus:")
for rank, (player, plus_minus) in enumerate(plusMinus_sorted.items(), start=1):
    print(f"{rank}. {player}: {plus_minus}")
