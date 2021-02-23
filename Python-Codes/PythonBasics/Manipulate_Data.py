import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


## read csv file 
df_Data =pd.read_csv("pokemon_data.csv")


#print first N rows
print(df_Data.head(7))

## Read headers
print(df_Data.columns)
## header values
cols = list(df_Data.columns.values)

## Print a specific column (here first 7 entries in "Name")
print(df_Data["Name"][0:7])
#(here first 7 entries in "Name" and "HP")
print(df_Data[["Name","HP"]][0:7])

## Print a specific row (here row 5)
print(df_Data.iloc[4])
# (here rows 5:7)
print(df_Data.iloc[4:8])


## Print only rows that satisfy a boolean condition 
print(df_Data.loc[df_Data["Type 1"] == "Fire"])
# here use 2 conditions
print(df_Data.loc[(df_Data["Type 1"] == "Fire") & (df_Data["Speed"] > 75)])
# & "and"
# | "or"
# ~  "not"

# >  "greater than"
# >=  "greater than or equal to"
# <  "less than"
# <=  "less than or equal to"
# ==  "equal to"
# !=  "not equal to"


## Print only entries whose name contains a specific string
print(df_Data.loc[df_Data["Name"].str.contains("Mega")]) 
## Print only entries whose name does not contains a specific string
print(df_Data.loc[~df_Data["Name"].str.contains("Mega")])




## regural expressions (Here string contains A or B)
import re
print(df_Data.loc[df_Data["Type 1"].str.contains("Fire|Grass", regex=True)])
# (Here all Pokemon starting with "Pi")
print(df_Data.loc[df_Data["Name"].str.contains("^Pi[a-z]*", regex=True)])


## Making a new data frame from an old one
df_Data_FIRE = df_Data.loc[df_Data["Type 1"] == "Fire"]
df_Data_FIRE.reset_index(inplace=True)    #Note: This line required to reset the index of new data frame
print(df_Data_FIRE)




## Summarise a data frame
df_Data.describe()
## groupby analysis
print(df_Data.groupby(["Type 1"]).mean())
print(df_Data.groupby(["Type 1"]).sum())
print(df_Data.groupby(["Type 1"]).mean().sort_values('Attack', ascending = False))

df_Data["count"] = 1
print(df_Data.groupby(["Type 1"]).count()['count'])
print(df_Data.groupby(["Type 1","Type 2"]).count()['count'])

## sort data frame first by Name (ascending) then by Speed (descending)
df_sorted_Data = df_Data.sort_values(["Name", "Speed"], ascending=[1,0])
print(df_sorted_Data.head(10))






## Add a column to the data frame
df_Data_New = df_Data.copy()
df_Data_New.reset_index(inplace=True)    #Note: This line required to reset the index of new data frame
#df_Data_New['Total stats'] = df_Data["HP"] + df_Data["Attack"] + df_Data["Defense"] + df_Data["Sp. Atk"] + df_Data['Sp. Def'] + df_Data["Speed"]
# Here add columns 
df_Data_New['Total stats'] = df_Data_New.iloc[:,5:11].sum(axis=1) #Here axis = 1 adds horizontally, axis = 0  adds vertically
print(df_Data_New.head(5))
# if total is less than 400 then set to none
df_Data_New.loc[df_Data_New['Total stats'] < 400, 'Total stats'] = None
print(df_Data_New.head(5))


## rename a columns in a dataframe
df_Data_New.rename(columns = {"Name": "Name_2"}, inplace=True)

## Save a data frame to csv/other
df_Data_New.to_csv('Pokemon_Modified.csv', index=False)
#df_Data_New.to_excel('Pokemon_Modified.xlsx', index=False)
#df_Data_New.to_csv('Pokemon_Modified.txt', index=False, sep = '\t')
print(df_Data_New.columns)


## Drop a column
df_Data_New = df_Data_New.drop(columns=["Total stats"])
## delete a data frame
del df_Data_New



## Merging two data frames
df_Data_2 =pd.read_csv("Pokemon_Modified.csv")
df_merged = pd.merge(df_Data, df_Data_2, left_on='Name', right_on='Name_2', how='outer')
print(df_merged.head(5))








