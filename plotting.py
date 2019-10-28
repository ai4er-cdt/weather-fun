#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 15:16:04 2019

@author: mwlw3
"""

import pandas
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import datetime as dt

data_file = "/home/mwlw3/Documents/Git_class/weather-fun/data_tidy.csv"
df = pandas.read_csv(data_file, index_col=0)
#%%
var_dict = {
        "humidity": "Humidity (%)",
        "pressure": "Pressure (mBar)",
        "avg_wind_bearing": "Average wind bearing (degrees)",
        "temp": "Temperature (Celsius)",
        "dew_point": "Dew Point (Celsius)",
        "mean_wind_speed": "Mean wind speed (knots)",
        "sunshine": "Sunshine (hours)",
        "rainfall": "Rainfall (mm)",
        "max_wind_speed": "Max wind speed (knots)"
        }

plotmax_dict = {
        "humidity": 110,
        "pressure": 1050,
        "avg_wind_bearing": 360,
        "temp": 40,
        "dew_point": 40,
        "mean_wind_speed": 50,
        "sunshine": 0.8,
        "rainfall": 10,
        "max_wind_speed": 80
        }
#%%
st_date = dt.date(2018,1,1)
ed_date = dt.date(2019,1,1)

fig, axs = plt.subplots(nrows=len(df.columns), ncols=1, sharex=False, figsize=(20,30))  
fig.subplots_adjust(hspace=0.5)

for i in range(len(df.columns)):
    col_name = df.columns[i]
    ax = axs[i]
    ax.plot(df.index, df[col_name], linewidth=0.5)
    ax.set_xlim(st_date, ed_date)
    ax.set_ylim(min(df[col_name]), plotmax_dict[col_name])
    ax.set_xlabel('Date')
    ax.set_ylabel(var_dict[col_name])
    ax.set_title("{} timeseries".format(col_name))

plt.show()
#%%
df.head()