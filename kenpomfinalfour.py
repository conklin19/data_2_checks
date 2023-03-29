### Adam Conklin ###
### Code Louisville ###
### Data Analytics 2 ###
### January 2023 ###

## Final Project ###
## KenPom College Basketball Analytics ###

import pandas as pd
import sqlite3
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_rows', None)


###  Requirement 4: Best Practices ###
###  4.1   Build a custom data dictionary (also in README) ##

conf_abbrev = {
    "ACC": "Atlantic Coastal",
    "AMR": "American",
    "B10": "Big 10",
    "B12": "Big 12",
    "BGE": "Big East",
    "COL": "Colonial",
    "HOR": "Horizon",
    "MVC": "Missouri Valley",
    "P12": "Pac 12",
    "SEC": "Southeastern",
    "WCC": "West Coast",
}


## Requirement 1: Loading Data ###
## 1.5  Set Up A Local Database and read data in with SQLite ##

conn = sqlite3.connect("assets/original.db")
c = conn.cursor()

sql = pd.read_sql_query("SELECT * FROM kenpom", conn)

df = pd.DataFrame(sql, columns = ["Year", "Team", "KPrank", "KPvalue", "Conference", "Champion"])

sql_2 = pd.read_sql_query("SELECT * FROM newtable", conn)

df2 = pd.DataFrame(sql_2, columns = ["Year", "Team", "Wins", "Losses", "Coach", "Nickname"])


### Requirement 2: Clean your data and perform a pandas merge with two data sets ###
### then calculate some new values based on the new data set ###

### Cleaning: Remove null values from 2020 (no tournament due to COVID-19) ###
df = df[df.Year != 2020]  

### Merge df and df2 based on matching Year and Team ###
df = pd.merge(df,df2, on=['Year','Team'])

### Cleaning: Round KPvalue to one decimal place instead of 2 ###
df['KPvalue'] = df['KPvalue'].astype(float).round(1)

### Cleaning: Move the Nickname Column to after the Team Column instead of being last ###

new_columns = ['Year', 'Team', 'Nickname', 'KPrank', 'KPvalue', 'Conference', 'Champion', 'Wins', 'Losses', 'Coach']

df = df[new_columns]

###New Value: Find the Most Losses by a National Champion ###
most_loss = float(df[['Losses']].max())
top_team = df.loc[df['Losses'] == most_loss]
print("The National Champion with the most losses is \n")
print(top_team)
print("\n")

### New Value: Find the Average Wins for a Final Four Team ###
mean_wins = int(df['Wins'].mean())
print('The average wins for all Final Four Teams is') 
print(mean_wins)
print('\n')

### Find the coach with the most Final Fours (mode of Coach Column) ###
mode_coach = (df['Coach'].mode())
print('The coach with the most Final Four teams is')
print(mode_coach)
print('\n')

print(df)


### Requirement 3 Visualization ###
### 3.3 Make at least 1 Pandas pivot table and 1 matplotlib/seaborn plot ###

champions = df.loc[df['Champion'] == 1]

champ_value = sns.lineplot(x= champions['Year'], y= df['KPvalue']).set(title='KenPom Value For Champions By Year')
champ_wins= sns.relplot(data=champions, x="Year", y="Wins").set(title= 'Wins Per Year for Champion By Year')

kp_pivot = df.pivot_table(index='Year', columns='Team', values='KPvalue')

print(kp_pivot)



