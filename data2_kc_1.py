## Adam Conklin ##
## Code Louisville ##
## Data Analytics 2 ##
## Knowledge Check 1 ##

import requests
import pandas as pd
import json

dataUSA = requests.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population')

df = pd.json_normalize(dataUSA.json()['data'])

print(df)



