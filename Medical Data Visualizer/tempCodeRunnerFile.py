import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('medical_examination.csv')

df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

df_cat = pd.melt(frame=df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

df_cat['total'] = 0
df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).count()
print(df_cat)

ax = sns.catplot(data=df_cat, x='variable', y='total', hue='value', kind='bar', col='cardio')

fig = ax.figure

fig.savefig('catplot.png')
