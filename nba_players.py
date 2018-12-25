import requests
import json
from bs4 import BeautifulSoup 
from csv import writer

"""
In this file we will attempt to scrape the stats for all players in the 2018 season
to see which college has the most players in the NBA 
"""

#response = requests.get("http://data.nba.net/10s/prod/v1/2018/players/203518_profile.json")

response = requests.get("http://data.nba.net/10s/prod/v1/2018/players.json")
soup = BeautifulSoup(response.text,"html.parser")
nba_player = str(soup)

# print(type(nba_player))

player = json.loads(nba_player)
# print(player["_internal"]["pubDateTime"])
#print(player["league"]["standard"]["stats"]["latest"]["seasonYear"])

# player_background = player["league"]["standard"][2]["collegeName"]
# # print(len(player_background))
# print(player_background)
# college = []
#test
with open("college_round1.csv","w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["firstName","lastName","collegeName","currentTeam","draftTeam","draftYear","yearsPro","position"])
    for item in player["league"]["standard"]:
    # print(item["collegeName"])
        firstName = item["firstName"]
        lastName = item["lastName"]
        collegeName = item["collegeName"]
        currentTeam = item["teams"]
        draftTeam = item["draft"]
        draftYear = item["nbaDebutYear"]
        yearsPro = item["yearsPro"]
        position = item["pos"]
        csv_writer.writerow([firstName,lastName,collegeName,currentTeam,draftTeam,draftYear,yearsPro,position])


#print(college)
# print(len(college))
# print(college)

