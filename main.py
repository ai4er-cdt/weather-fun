import requests
import csv
import pandas
import matplotlib.pyplot as plt
import os
import time

from helper_functions import save_csv_from_url

url = "https://www.cl.cam.ac.uk/research/dtg/weather/weather-raw.csv"
data_file = "data.csv"

if not os.path.exists(data_file):
	save_csv_from_url(url, data_file)

# Fetch data if it is more than one day out of date 
today = time.time() 
mtime = os.path.getmtime(data_file) 
if mtime + (24*60*60) < today:
	save_csv_from_url(url, data_file)

headers = ["Timestamp","Temperature","Humidity","DewPoint","Pressure",
		   "MeanWindSpeed","WindBearing","Sunshine","Rainfall","MaxWindSpeed"]

df = pandas.read_csv(data_file, names=headers)	
df['Timestamp'] = pandas.to_datetime(df['Timestamp'])
df['Temperature'] = pandas.to_numeric(df['Temperature'])
df = df.set_index('Timestamp')

# Convert data to appropriate units 
df[['Temperature','DewPoint']] *= 0.1  # to degrees Celsius
df[['MeanWindSpeed', 'MaxWindSpeed']] *= 0.1 * 0.514444  # to m/s 
df['Sunshine'] *= 0.01  # to hours
df['Rainfall'] *= 1e-3  # to mm

#df = df.resample('D')

print(df)
