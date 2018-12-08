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

player_background = player["league"]["standard"][2]["collegeName"]
# print(len(player_background))
print(player_background)



# print(d[])


# with open("blog_data.csv","w") as csv_file:
#     csv_writer = writer(csv_file)
#     csv_writer.writerow(["title","link","date"])
#     for article in articles:
#         a_tag = article.find("a")
#         title = a_tag.get_text()
#         url = a_tag['href']
#         date = article.find("time")["datetime"]
#         # print(title,url,date)
#         csv_writer.writerow([title,url,date])

