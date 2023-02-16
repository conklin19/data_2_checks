## Adam Conklin ##
## Code Louisville ##
## Data Analytics 2 ##
## Knowledge Check 1 ##


### Import Libraries ###
import requests
import pandas as pd
import json


### First Requirement: Pull in data from an API ###
### I used the link provided in the assignment and pulled in ###
### recent USA population data from 2013-2020 ###
dataUSA = requests.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population')

### Convert the imported API json to a pandas dataframe ###
df = pd.json_normalize(dataUSA.json()['data'])

### Second Requirement: Find and print TWO descriptive statistics about your data ###
### I will focus on the Population Column by finding the mean and standard deviation ###

mean_population = int(pd.DataFrame.mean(df["Population"]))
stdev_population = int(pd.DataFrame.std(df["Population"]))

print('The mean USA Population from 2013-2020 is')
print(mean_population)
print('\n')
print('The standard deviation of the USA Population from 2013-2020 is')
print(stdev_population)

### Third Requirement: Write a Query in Pandas ###
### I will pull out the years that had population above the average ###
### as determiined earlier in the file ###
pop_query = df.query('Population > 319486425')
print(pop_query)

### Fourth Requirement: Select and Print the Second and Third Columns of your DataFrame ###
print(df.loc[:, "Nation":"ID Year"])

### Fifth Requirement: Select and Print the First Four Rows of your DataFrame###
print(df.loc[0:3, :])





      








