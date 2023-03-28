### Adam Conklin ###
### Code Louisville ###
### Data Analytics 2 ###
### January 2023 ###

## Final Project ###
## Advanced KenPom College Basketball Analytics ###

import pandas as pd
import sqlite3
import pandasql as ps

## Requirement 1: Loading Data ###
## Set Up A Local Database and read data in with SQLite ##

conn = sqlite3.connect("assets/original.db")
c = conn.cursor()

sql = pd.read_sql_query("SELECT * FROM kenpom", conn)

df = pd.DataFrame(sql, columns = ["Year", "Team", "KPrank", "KPvalue", "Conference", "Champion"])

sql_2 = pd.read_sql_query("SELECT * FROM newtable", conn)

df2 = pd.DataFrame(sql_2, columns = ["Year", "Team", "Wins", "Losses", "Coach", "Nickname"])


### Requirement 2: Clean your data and perform a pandas merge with two data sets ###
### then calculate some new values based on the new data set ###
combined = pd.merge(df, df2, on= 'Year', how= 'outer', suffixes=['_l','_r'])

print(combined)

