import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    first_line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_values = pd.DataFrame(range(1880, 2051))
    y_values = first_line.intercept + (first_line.slope * x_values)
    plt.plot(x_values, y_values)

    # Create second line of best fit
    second_line = linregress(df['Year'][df['Year'] >= 2000], df['CSIRO Adjusted Sea Level'][df['Year'] >= 2000])
    x_values = pd.DataFrame(range(2000, 2051))
    y_values = second_line.intercept + (second_line.slope * x_values)
    plt.plot(x_values, y_values)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')    
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()