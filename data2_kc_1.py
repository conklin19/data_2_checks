## Adam Conklin ##
## Code Louisville ##
## Data Analytics 2 ##
## Knowledge Check 1 ##

import requests

dataUSA = requests.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population')
print(dataUSA.json())



