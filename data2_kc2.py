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
