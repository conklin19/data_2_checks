## Code Louisville ##
## Data Analytics Course 1 ##
## September 2022 Cohort ##
## Adam Conklin- Final Project ##
## Analyzing Pomeroy Data on teams that made the NCAA Final Four ##

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('assets\KenPomData.csv')

print(df['Year'][0:5])
