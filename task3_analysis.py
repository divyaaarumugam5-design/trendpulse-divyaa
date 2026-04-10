#==================Analysis============================================
import requests
import time
from datetime import datetime
import json
import pandas as pd
import numpy as np 
## Task 3.1

df_original=pd.read_csv("data/trends_clean.csv")
print(f"First five rows:\n{df_original.head(5)}")
print(f"Shape of the dataset:{df_original.shape}")
print(f"Average score:{round(df_original["score"].mean(),2)}\nAverage num_comments:{round(df_original["num_comments"].mean(),2)}")

## Task 3.2
arr=np.array(df_original["score"])
print(f"Mean of the score:{round(np.mean(arr))}\nMedian of the score:{round(np.median(arr))}\nStandard Deviation of the score:{round(np.std(arr))}")
print(f"Highest score:{np.max(arr)}\nLowest score:{np.min(arr)}")

#Using numpy  fetching category most stories using unique commad and agrmax()
category,counts=np.unique(df_original["category"],return_counts=True)
print(f"Category with most stories:{category[np.argmax(counts)]}({counts[0]} stories)")

#Using numpy  fetching stories most comments using unique commad and agrmax()
comments=np.array(df_original["num_comments"])
title=np.array(df_original["title"])
print(f"Stories with maximum comments:{title[np.argmax(comments)]}- {comments[0]} comments")


## Task 3.3

df_original["engagement"]=((df_original["num_comments"])/(df_original["score"]+1))
df_original["is_popular"]=df_original["score"]>df_original["score"].mean()
# print(df_original[["title","score","engagement","is_popular"]].head())

## Task 3.4
df_original.to_csv("data/trends_analysed.csv")
print("File loaded Successfully!")

############################################################################################################################
