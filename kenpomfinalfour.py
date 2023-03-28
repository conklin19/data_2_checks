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
print(df2)

### Requirement 2: Clean your data and perform a pandas merge with two data sets ###
### then calculate some new values based on the new data set ###
combined = sql.merge(sql_2, left_on= 'Year', right_on='Year')

### Clean by deleting duplicate/redundant rows ###
combined.drop(['id_x','id_y', 'Team_y'], axis = 1, inplace = True)


### Rename column header ###
combined.rename(columns = {'Team_x':'Team'}, inplace=True)

print(combined)



