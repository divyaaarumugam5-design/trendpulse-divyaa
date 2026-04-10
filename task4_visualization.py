#=================Visualization====================================
import requests
import time
from datetime import datetime
import json
import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt


#Task1
df_visual=pd.read_csv("data/trends_analysed.csv")
# df_visual.shape

#Task2
top_stories=df_visual.sort_values(by="score",ascending=False).head(10).reset_index()
# print(top_stories)
# x=top_stories["score

plt.barh(top_stories["title"].str[:50],top_stories["score"])
plt.title("Top 10 Stories by  Score")
plt.xlabel("Score")
plt.ylabel("Title")
plt.savefig("outputs/chart1_top_stories.png",bbox_inches="tight")
# plt.show()
#Task 3
count=df_visual["category"].value_counts()
# print(count.index)
# columns=count.index
plt.bar(count.index, count.values, color=["blue","red","green","orange","purple"])
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")
plt.savefig("outputs/chart2_categories.png",bbox_inches="tight")
# plt.show()


#Task 4

#print(df_visual)
popular = df_visual[df_visual["is_popular"] == True]
not_popular = df_visual[df_visual["is_popular"] == False]
#Fetching scatter plots for popular and not popular
plt.scatter(popular["score"], popular["num_comments"], color="orange", label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], color="brown", label="Not Popular")

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend() 
plt.savefig("outputs/chart3_scatter.png",bbox_inches="tight")
# plt.show()

# Task 4 

fig, ax = plt.subplots(1, 3, figsize=(18, 5)) 
#Chart 1  
ax[0].barh(top_stories["title"].str[:50],top_stories["score"])
ax[0].set_xlabel("Score")
ax[0].set_ylabel("Title")
ax[0].set_title("Top 10 Stories by  Score")

#Chart 2
ax[1].bar(count.index, count.values, color=["blue","red","green","orange","purple"])
ax[1].set_xlabel("Category")
ax[1].set_ylabel("Number of Stories")
ax[1].set_title("Stories per Category")

# Chart 3
ax[2].scatter(popular["score"], popular["num_comments"], color="orange", label="Popular")
ax[2].scatter(not_popular["score"], not_popular["num_comments"], color="brown", label="Not Popular")
ax[2].set_xlabel("Score")
ax[2].set_ylabel("Number of Comments")
ax[2].set_title("Score vs Comments")
ax[2].legend() 

plt.suptitle("TrendPusle Dashboard")
plt.tight_layout()
plt.savefig("outputs/dashboard.png")
# plt.show()