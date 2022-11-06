##Adam Conklin ###
## Code Louisville ###
### Data Analysis 1 ###
### September 2022 Cohort ###

### Knowlege Check 2 ##

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\conkl\OneDrive\Documents\PythonScripts\data_1_checks\assets\KC_2_data.csv')
df.head()

print(df)

plt.plot(df.Game, df.Points_Scored)
plt.show()







