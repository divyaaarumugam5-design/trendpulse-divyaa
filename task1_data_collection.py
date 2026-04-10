import requests
import time
from datetime import datetime
import json
import pandas as pd
import numpy as np 


url="https://hacker-news.firebaseio.com/v0/topstories.json"
headers = {"User-Agent": "TrendPulse/1.0"}

response=requests.get(url,headers=headers)
if response.status_code==200:
    data=response.json()
    top_id=data[:500]
    
else:
    print("Data fecth Failed!")
 

stories=[]
for i in top_id:
    try:
      response2=requests.get(f"https://hacker-news.firebaseio.com/v0/item/{i}.json",headers=headers)
      if response2.status_code==200:
        data=response2.json()
        stories.append(data)
      else:
        print("Data Fetch Failed")
      time.sleep(0.5)
    except requests.exceptions.RequestException as e:
      print(f"Error:{e}")
      continue

#Task1 

# category={"technology":["AI","software","tech","code","computer","data","cloud","API","GPU","LLM"],
#           "worldnews":["war","government","country","president","election","climate","attack","global"],
#           "sports":["NFL","NBA","FIFA","sport","game","team","player","league","championship"],
#           "science":["research","study","space","physics","biology","discovery","NASA","genome"],
#           "entertainment":["movie","film","music","Netflix","game","book","show","award","streaming"]}
category = {
    "technology": ["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"],
    "worldnews": [
        "war", "government", "country", "president", "election", "climate", "attack",
        "global", "police", "law", "trade", "military", "missile", "import", "export",
        "senate", "congress", "treaty", "sanction", "border", "refugee", "protest",
        "minister", "crisis", "diplomat", "conflict", "nation", "international",
        "relations", "summit", "UN", "NATO", "china", "russia", "usa", "israel",
        "palestine", "ukraine", "economy", "inflation", "policy"
    ],
     "sports": [
        "NFL", "NBA", "FIFA", "sport", "game", "team", "player", "league",
        "championship", "winner", "athlete", "coach", "cricket", "IPL",
        "football", "soccer", "olympics", "score", "tournament", "final",
        "batting", "bowling", "goal", "transfer", "injury", "match",
        "tennis", "badminton", "formula", "race", "cup", "series",
        "captain", "squad", "win", "loss", "draw"
    ],
    "science": [
        "research", "study", "space", "physics", "biology", "discovery",
        "NASA", "genome", "experiment", "scientist", "genetics",
        "quantum", "radiation", "vaccine", "virus", "cancer",
        "protein", "clinical", "trial", "asteroid", "telescope",
        "fossil", "evolution", "chemistry", "lab", "analysis",
        "data", "theory", "environment", "earth", "planet",
        "galaxy", "astronomy", "microscope", "innovation"
    ],
    "entertainment": ["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"]
}


assigned_cat={"technology":[],"worldnews":[],"sports":[],"science":[],"entertainment":[]}

for cat,key in category.items():
  time.sleep(2)

  for i in stories:
  #print(i["title"])

    
     for j in i["title"].split():

      if j.lower() in  [item.lower() for item in key]:
        if cat in assigned_cat:
          assigned_cat[cat].append(i["title"])
        else:
          assigned_cat[cat]=i["title"]
# print (assigned_cat["technology"])

# for cat,title in assigned_cat.items():
#   print(cat,len(title))

#Task 2
new_set={"technology":[],"worldnews":[],"sports":[],"science":[],"entertainment":[]}
for cat,key in category.items():
  time.sleep(2)
  for i in stories:
    for j in i["title"].split():
      if j.lower() in [item.lower() for item in key]:
        if cat in new_set:
          new_set[cat].append(i)
        else:
          new_set[cat]=i

# for cat,key in new_set.items():
#   print(cat,len(key))
final_one=[]
descendats_error=[]
for cat,key in new_set.items():
  for i in key[:25]:
    # print(i)
    if "descendants" not in i:
      descendats_error.append(i)
    temp={"post_id":i["id"],
          "title":i["title"],
          "category":cat,
          "score":i["score"],
          "num_comments":i.get("descendants",0), 
          # Key error given so based on data fecthed add 0 if descendants not in list
          "author":i["by"],
          "collected_at":datetime.now().strftime("%Y-%m-%d %H:%M:%S")# added because while saving json file shows error coverted to string 


    }
    final_one.append(temp)
# print(final_one)
# print(len(descendats_error))

#Task 3
print(f"Collected {len(final_one)} stories. Saved to data/trends20260410.json")
with open("data/trends_20260410.json","w") as file:
   json.dump(final_one,file,indent=4)



#############################################################################################################################



