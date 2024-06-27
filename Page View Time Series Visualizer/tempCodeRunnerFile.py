
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=True, index_col='date')
df = df.drop(df[(df.value < df.value.quantile(0.025)) | (df.value > df.value.quantile(0.975))].index)

df_box = df.copy()
df_box.reset_index(inplace=True)
df_box['year'] = [d.year for d in df_box.date]
df_box['month'] = [d.strftime('%b') for d in df_box.date]

# Draw box plots (using Seaborn)
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(25, 8))

sns.boxplot(data=df_box, x='year', y='value', hue='year', ax=axes[0], legend=False)
axes[0].set_title('Year-wise Box Plot (Trend)')
axes[0].set_xlabel('Year')
axes[0].set_ylabel('Page Views')

month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 
                'Sep', 'Oct', 'Nov', 'Dec']
sns.boxplot(data=df_box, x='month', y='value', hue='month', ax=axes[1], order=month_order)
axes[1].set_title('Month-wise Box Plot (Seasonality)')

axes[1].set_xlabel('Month')
axes[1].set_ylabel('Page Views')


# Save image and return fig (don't change this part)
fig.savefig('box_plot.png')
#return fig
