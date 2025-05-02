import pandas as pd
import json

def transform_data(user_input: dict) -> dict:
    teams = [
    "ATL", "BOS", "BRK", "CHI", "CHO", "CLE", "DAL", "DEN", "DET", "HOU",
    "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOP", "NYK", "OKC",
    "ORL", "PHI", "PHO", "POR", "SAC", "SAS", "TOR", "UTA", "WAS"]

    designation = ["away", "home"]
    
    opp_dict = {f"Opp_{team}": 1 if user_input["opponent"] == team else 0 for team in teams}

    designation_dict = {f"designation_{desig}": 1 if user_input["designation"] == desig 
                        else 0 for desig in designation}
    

    stats_dict = {
        "FG": float(user_input["FG"]),
        "FGA": float(user_input["FGA"]),
        "FG%": float(user_input["FG%"]),
        "3P": int(user_input["3P"]),
        "3PA": float(user_input["3PA"]),
        "3P%": float(user_input["3P%"]),
        "2P": int(user_input["2P"]),
        "2PA": float(user_input["2PA"]),
        "2P%": float(user_input["2P%"]),
        "eFG%": float(user_input["eFG%"]),
        "FT": int(user_input["FT"]),
        "FTA": float(user_input["FTA"]),
        "TOV": int(user_input["TOV"]),
        "PF": int(user_input["PF"]),
        "GmSc": float(user_input["GmSc"]),
    }


    return {**stats_dict, **designation_dict, **opp_dict}

# user_input = {

#     "FG": "12",
#     "FGA": "23",
#     "FG%": "0.522",
#     "3P": "5",
#     "3PA": "13",
#     "3P%": "0.385",
#     "2P": "7",
#     "2PA": "10",
#     "2P%": "0.7",
#     "eFG%": "0.63",
#     "FT": "7",
#     "FTA": "8",
#     "TOV": "2",
#     "PF": "0",
#     "GmSc": "33.1",
#     "opponent": "SAS",     
#     "designation": "home"    
# }

# row = transform_data(user_input)
# json_output = json.dumps(row, indent=2)
# print(json_output)