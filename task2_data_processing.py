#=========================Data cleaning========================
import requests
import time
from datetime import datetime
import json
import pandas as pd
import numpy as np 
# # Task 2.1
with open("data/trends_20260410.json","r") as file:
  
  loaded_data=json.load(file)
# print(type(loaded_data))
df=pd.DataFrame(loaded_data)
df.head(5)
# no_of_rows=df.shape()
print(f"Total number of rows:{len(df)}")


# Task 2.2
# len(df[df["post_id"].duplicated()])

##Removing duplicate rows with same post id
# print(f"Shape before removing duplicates with same post id:{len(df)},{df.shape}")
df_clean=df.drop_duplicates(subset="post_id")
# print(f"Shape before removing duplicates with same post id:{len(df_clean)},{df_clean.shape}")

##Missing values - dropping rows where post id, title,score is missing 
# print(f"Shape before removing duplicates with same post id:{len(df_clean)},{df_clean.shape}")
df_cleaning=df_clean.dropna(subset=["post_id","score","title"])
# print(f" before removing duplicates with same post id:{len(df_cleaning)},{df_cleaning.shape}")


##Data types — make sure score and num_comments are integers
# print(f"Datatypes before:{df_cleaning.dtypes}")
df_cleaning["score"]=pd.to_numeric(df_cleaning["score"],errors="coerce")
df_cleaning["num_comments"]=pd.to_numeric(df_cleaning["num_comments"],errors="coerce")
df_cleaning["collected_at"]=pd.to_datetime(df["collected_at"],errors="coerce")
# print(f"Datatypes before:{df_cleaning.dtypes}")


##Remove stories score is less than 5

df_cleaning=df_cleaning[df_cleaning["score"]>=5]
# print(f"Shape before removing duplicates with same post id:{len(df_cleaning)},{df_cleaning.shape}")


df_cleaning["title"]=df_cleaning["title"].str.strip()


df_cleaned=df_cleaning
# print(df_cleaned.shape)
print(f"Total number of rows after cleaning:{len(df_cleaned)}")

# Task 2.3
df_cleaned.to_csv("data/trends_clean.csv",index=False)
print(f"Cleaned Data loaded saved as csv file with {len(df_cleaned)} rows")
print("\nStories Per category\n")
print(df_cleaned["category"].value_counts().reset_index())


############################################################################################################################