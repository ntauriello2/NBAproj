import requests
import json

url = "https://api-nba-v1.p.rapidapi.com/players/statistics"

querystring = {"team":"2","season":"2023"}

headers = {
	"X-RapidAPI-Key": "01c90681b6msh2b10242e9649c00p1507d2jsn20e0d2354ba8",
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)


r = response.json

file_path = "response.json"
nickname = r["response"][0]["team"]["nickname"]

# Write the JSON response to the file
with open(nickname, "w") as json_file:
    json.dump(response.json(), json_file)