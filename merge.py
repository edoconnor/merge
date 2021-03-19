import pandas as pd
import csv

df = pd.read_csv("scores1.csv") 
df = df[['player', 'RSF']]
x = df.rename(columns={'RSF': 'date'})

df2 = pd.read_csv("scores2.csv") 
df2 = df2[['player', 'RSF']]
y = df2.rename(columns={'RSF': 'date'})

result = x.merge(y, left_on='player', right_on='player', how='outer')

print(result)

df3 = result
df3.to_csv('results1.csv')
#---------------------------------------------------
##comment out below while using top -->
#---------------------------------------------------
df = pd.read_csv("results1.csv") 
df = df[['player', 'date1', 'date2']]

df2 = pd.read_csv("results2.csv") 
df2 = df2[['player', 'date1', 'date2']]

df3 = df.merge(df2, left_on='player', right_on='player', how='outer')

result = df3.drop(['Unnamed: 0_x', 'Unnamed: 0_y'], axis=1)

print(df3)

df3.to_csv('combined1.csv')
#---------------------------------------------------