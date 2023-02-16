## Adam Conklin ##
## Code Louisville ##
## Data Analytics 2 ##
## Knowledge Check 1 ##

import requests

dataUSA = requests.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population')

population = dataUSA.json()['data'][4]['Population']
print(population)




