#Weather data visualization Project

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

bengaluru='bengaluru-temp-rains.csv'
delhi='delhi-temp-rains.csv'
kolkata='kolkata-temp-rains.csv'
pune='pune-temp-rains.csv'



#creating function

csvs=[bengaluru,delhi,kolkata,pune]
cities=["Bengaluru","Delhi","Kolkata","Pune"]
for i in range(len(csvs)):
    data= pd.read_csv(csvs[i])

    print(f"{cities[i]}")

#Using time functions
    data['Date'] = pd.to_datetime(data['Date'],format='%d-%m-%Y')  # Convert the 'Date' column to datetime

# Step 3: Add Year and Month columns for grouping
    data['Temperature']=pd.to_numeric(data['Temp Max'],errors='coerce')
    data['Rain']=pd.to_numeric(data['Rain'],errors='coerce')
    data['Year'] = data['Date'].dt.year
    data['Month'] = data['Date'].dt.month

# Step 4: Calculate yearly average temperature (or other weather metrics)
    globals()[f'yearly_data_{cities[i]}'] = data.groupby('Year')['Temperature'].mean()
    globals()[f'precipitation_{cities[i]}'] = data.groupby('Year')['Rain'].mean()

# Step 5: Visualizing the data

# Plotting the average yearly temperature over 50 years
plt.figure(figsize=(12, 6))
plt.plot(yearly_data_Bengaluru.index, yearly_data_Bengaluru.values, color='b', label='Bengaluru Avg Temp (°C)')
plt.plot(yearly_data_Delhi.index, yearly_data_Delhi.values, color='m', label='Delhi Avg Temp (°C)')
plt.plot(yearly_data_Kolkata.index, yearly_data_Kolkata.values, color='y', label='Kolkata Avg Temp (°C)')
plt.plot(yearly_data_Pune.index, yearly_data_Pune.values, color='c', label='Pune Avg Temp (°C)')
plt.title(f'Yearly Average Temperature Over 50 Years', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Temperature (°C)', fontsize=12)
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plotting the average yearly Rainfall over 50 years
plt.figure(figsize=(12, 6))
plt.plot(precipitation_Bengaluru.index, precipitation_Bengaluru.values, color='c', label='Bengaluru Precipitation (cm)')
plt.plot(precipitation_Delhi.index, precipitation_Delhi.values, color='g', label='Delhi Precipitation (cm)')
plt.plot(precipitation_Kolkata.index, precipitation_Kolkata.values, color='r', label='Kolkata Precipitation (cm)')
plt.plot(precipitation_Pune.index, precipitation_Pune.values, color='k', label='Pune Precipitation (cm)')
plt.title(f'Yearly Average Precipitation Over 50 Years', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Rainfall (cm)', fontsize=12)
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
