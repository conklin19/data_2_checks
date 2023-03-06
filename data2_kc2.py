### Adam Conklin ###
### Code Louisville ###
### Data Analytics 2 ###
### January 2023 ###

### Knowledge Check 2: Data Cleaning ###

import requests
import pandas as pd


## Pull in United States Population Data from Knowledge Check 1 ###

dataUSA = requests.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population')

### Convert the imported API json to a pandas dataframe ###

df = pd.json_normalize(dataUSA.json()['data'])

print(df)

### Make a Copy of the original dataframe ###
clean_df = df

### First Clean: Delete redundant column 'ID Year' because we don't need the year twice ###
clean_df = clean_df.drop(['ID Year'], axis = 1)

print(clean_df)

### Second Clean: Replace erroneous values to a simple 1 ###
clean_df['ID Nation'].replace('01000US', '1', inplace=True)

###Third Clean: Put full name of the country in instead of just United States ###
clean_df['Nation'].replace('United States', 'United States of America', inplace=True)

### Fourth Clean: Change erroneous Slug Nation column to an abbreviation of the country name ###
clean_df.rename(columns = {'Slug Nation':'Abbreviation'}, inplace=True)

### Fifth Clean: change values in Abbrevation column to USA ###
clean_df['Abbreviation'].replace('united-states','USA', inplace=True)


print(clean_df)






