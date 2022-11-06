##Adam Conklin ###
## Code Louisville ###
### Data Analysis 1 ###
### September 2022 Cohort ###

### Knowlege Check 2 ##

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('assets/Conklin_KC_2data.csv')
df.head()

print(df)

plt.plot(df.Game, df.Points_Scored)
plt.title('Purdue Football Points Scored Per Game')
plt.xlabel('Game')
plt.ylabel('Points Scored')
plt.show()








