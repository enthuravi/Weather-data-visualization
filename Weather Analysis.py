#Weather data visualization Project

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

bengaluru='bengaluru-temp-rains.csv'
delhi='delhi-temp-rains.csv'
kolkata='kolkata-temp-rains.csv'
pune='pune-temp-rains.csv'

#creating function
def visualize(data,city):

    print(f"{city}")

#Using time functions
    data['Date'] = pd.to_datetime(data['Date'],format='%d-%m-%Y')  # Convert the 'Date' column to datetime

# Step 3: Add Year and Month columns for grouping
    data['Temperature']=pd.to_numeric(data['Temp Max'],errors='coerce')
    data['Rain']=pd.to_numeric(data['Rain'],errors='coerce')
    data['Year'] = data['Date'].dt.year
    data['Month'] = data['Date'].dt.month

# Step 4: Calculate yearly average temperature (or other weather metrics)
    yearly_data = data.groupby('Year')['Temperature'].mean()
    precipitation = data.groupby('Year')['Rain'].mean()

# Step 5: Visualizing the data

# Plotting the average yearly temperature over 50 years
    plt.figure(figsize=(12, 6))
    plt.plot(yearly_data.index, yearly_data.values, color='b', label='Avg Temp (°C)')
    plt.title(f'{city}\nYearly Average Temperature Over 50 Years', fontsize=16)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Average Temperature (°C)', fontsize=12)
    plt.grid(True)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Plotting the average yearly Rainfall over 50 years
    plt.figure(figsize=(12, 6))
    plt.plot(precipitation.index, precipitation.values, color='c', label='Avg Precipitation (cm)')
    plt.title(f'{city}\nYearly Average Precipitation Over 50 Years', fontsize=16)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Average Rainfall (cm)', fontsize=12)
    plt.grid(True)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Plotting monthly averages or other types of analysis
    monthly_data = data.groupby(['Year', 'Month'])['Temperature'].mean()

# temperature for a specific year (e.g., 2020)
    plt.figure(figsize=(10, 5))
    year_show=2015
    monthly_2020 = monthly_data[year_show]
    plt.plot(monthly_2020.index, monthly_2020.values, marker='o', linestyle='-', color='r', label=f'{year_show} Avg Temp (°C)')
    plt.title(f'{city}\nMonthly Average Temperature in {year_show}', fontsize=16)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Average Temperature (°C)', fontsize=12)
    plt.xticks(np.arange(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

#calling function
csvs=[bengaluru,delhi,kolkata,pune]
cities=["Bengaluru","Delhi","Kolkata","Pune"]
for i in range(len(csvs)):
    data = pd.read_csv(csvs[i])
    visualize(data,cities[i])
