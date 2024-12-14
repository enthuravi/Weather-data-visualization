#Weather data visualization Project

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('bengaluru-temp-rains.csv')

print("The case of bengaluru\n--_--_--_--_--_--_--_--_--_--_--_--")

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
plt.title(f'Bengaluru\nYearly Average Temperature Over 50 Years', fontsize=16)
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
plt.title('Bengaluru\nYearly Average Precipitation Over 50 Years', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Rainfall (cm)', fontsize=12)
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

climate_year=[]
for i in range(44):
    climate_year.append(1980+i)
    

_temp=yearly_data.values.tolist()
temp=0
list_temp=[]
for i in range(44):
    for j in range(i,i+30):
        temp+=_temp[j]
    temp=temp/30
    list_temp.append(temp)

_ppt=precipitation.values.tolist()
ppt=0
list_ppt=[]
for i in range(44):
    for j in range(i,i+30):
        ppt+=_ppt[j]
    ppt=ppt/30
    list_ppt.append(ppt)

plt.figure(figsize=(12, 6))
plt.plot(climate_year,list_temp, color='g', label="temperature")
plt.title('Bengaluru climate', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Climatic Temperature (°C)', fontsize=12)
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(climate_year,list_ppt, color='m', label="Precipitation")
plt.title('Bengaluru climate', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Climatic Rainfall (cm)', fontsize=12)
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
plt.title(f'Bengaluru\nMonthly Average Temperature in {year_show}', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Average Temperature (°C)', fontsize=12)
plt.xticks(np.arange(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.legend()
plt.grid(True)
plt.tight_layout()
#plt.show()
