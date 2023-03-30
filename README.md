# data_2_finalproject
knowledge checks for CodeLou

Adam Conklin Code Louisville Data Analytics 2 January 2023 Cohort

Final Project README KenPom College Basketball Analytics

Project Requirements that are met in this project:

Loading Data- Option 5: Set Up a Local Database and read data in with SQLite or SQLAlchemy

Cleaning Data- Option 1: Clean your data and perform a pandas merge with your two data sets, then calculate some new values (Changed from Option 3: Perform a SQL join or pandasql join)

Visualize- Option 3: Make at least one pandas pivot table and one matplotlib/seaborn plot (Changed from Option 2 Tableau Dashboard)

Best Practices- Option 3: Build a custom data dictionary (since this is custom data that I built) (Changed from Option 2 - Write 3 unit tests)

Interpretation- Option 2- Annotate .py file with well-written comments and a README file

In this project, I used data from the website kenpom.com which is an advanced college basketball data analytic used by professionals to predict game scores and spreads in the betting world. In my project for Data 1, I created a csv of the teams that made the NCAA Tournament Final Four from 2002(the earliest year of record for the analytic) all the way to 2022. There were a total of 84 rows: 4 teams from each year that was reduced to 80 rows after deleting the 2020 records because the tournament was cancelled due to COVID-19. The columns in this dataframe were as follows. (This original data became known as the table 'kenpom' in the SQL database for this project)

Year- 2002 through 2022 (except 2020) Team- The School that made the Final Four KPrank- The kenpom ranking of the team compared to the rest of the country (Divison 1 only) KPvalue- The kenpom rating of the team Conference- The conference the team represents (abbreviated in the database with a dictionary) Champion- A '1' in this column indicates the National Champion for that year; a '0' indicates a non-champion

This data is the 'kenpom' dataframe in this project

In the first project, the data above was in a .csv file. I downloaded DB Browser and created a database for this project. The data above is in a table called 'kenpom'. The new data is in a table called 'newtable'. This contains additional information to add to the rows of 'kenpom' as follows

Wins- The team's total wins for the season Losses- The team's total losses for the season Nickname- The team's school nickname (Official Nickname) Coach- The Team's coach.

I manually entered the data into the two tables, 'kenpom', and 'newtable' and then began my code.

I imported the libraries as follows

import pandas as pd import sqlite3 import seaborn as sns import matplotlib.pyplot as plt import numpy as np

I satisfied requirement 4 by creating a dictionary to relate the conference abbreviations to the conference name as follows

conf_abbrev = { "ACC": "Atlantic Coastal", "AMR": "American", "B10": "Big 10", "B12": "Big 12", "BGE": "Big East", "COL": "Colonial", "HOR": "Horizon", "MVC": "Missouri Valley", "P12": "Pac 12", "SEC": "Southeastern", "WCC": "West Coast", }

Requirement 1: read in data and Requirement 2: Clean Data/Calculate new values I then used SQLite to read in the two tables from the database and converted each of the to pandas dataframes. I first cleaned the data by deleting the 2020 records because there was no NCAA tournament due to COVID-19. Then, I performed a pandas merge on line 58 using the Year and Team to ensure no additional rows were created. I ended up with 80 rows and manually inspected them to ensure the merged dataframe (df) was correct.

I cleaned the data as follows: (beginning line 54) -Removed null 2020 values -Rounded KPvalue from two decimals to one decimal place -Moved the Nickname Column to follow the team column instead of being out on the end

I calculated new values as follows: (beginning line 69) -The most losses by a National Champion (Syracuse 2016) -The average wins for a Final Four Team (31) -The coach with the most Final Fours (Roy Williams- Kansas/North Carolina) -The average kenpom rank for Final Four Teams (7.85)

Requirement 3: Visualization

Line 101- I created the x-axis list of ONLY the national champions by using pandas loc

I used seaborn/matplotlib to plot the KPvalue of the national champions by year.

I then created a pivot table of all the schools represented but only with the KPvalue of their Final Four Teams.
