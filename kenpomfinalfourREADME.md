Adam Conklin
Code Louisville
Data Analytics 2
January 2023 Cohort

Final Project README
KenPom College Basketball Analytics

Project Requirements that are met in this project:

1. Loading Data- Option 5: Set Up a Local Database and read data in with SQLite or SQLAlchemy

2. Cleaning Data- Option 1: Clean your data and perform a pandas merge with your two data sets, then calculate some new values
(Changed from Option 3: Perform a SQL join or pandasql join)

3. Visualize- Option 3: Make at least one pandas pivot table and one matplotlib/seaborn plot
(Changed from Option 2 Tableau Dashboard)

4. Best Practices- Option 3: Build a custom data set (since this is custom data that I built)
(Changed from Option 2 - Write 3 unit tests)

5. Interpretation- Option 2- Annotate .py file with well-written comments and a README file

In this project, I used data from the website kenpom.com which is an advanced college basketball data analytic used by professionals to predict game scores and spreads in the 
betting world. In my project for Data 1, I created a csv of the teams that made the NCAA Tournament Final Four from 2002(the earliest year of record for the analytic) all the way to
2022. There were a total of 84 rows: 4 teams from each year that was reduced to 80 rows after deleting the 2020 records because the tournament was cancelled due to COVID-19. The columns 
in this dataframe were as follows. (This original data became known as the table 'kenpom' in the SQL database for this project)

Year- 2002 through 2022 (except 2020)
Team- The School that made the Final Four
KPrank- The kenpom ranking of the team compared to the rest of the country (Divison 1 only)
KPvalue- The kenpom rating of the team
Conference- 
