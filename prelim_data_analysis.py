
# coding: utf-8

# In[1]:


import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import glob
import re


# In[11]:


data_format = ["Timestamp (GMT)", "Temperature (Celsius)", "Humidity (%)", "Dew Point (Celsius)", 
               "Pressure (mBar)", "Mean wind speed (knots)", "Average wind bearing (degrees)", "Sunshine (hours)", 
               "Rainfall (mm)", "Max wind speed (knots)"]


# In[14]:


data_labels = ["time", "temp_10", "humidity", "dew_point_10", 
               "pressure", "mean_wind_speed_10", "avg_wind_bearing", "sunshine_100", 
               "rainfall_1000", "max_wind_speed_10"]


# In[73]:
def folder_path(computer):
    if computer == "work":
        path = "/home/mwlw3/Documents/Git_class/weather-fun/"
    elif computer == "home":
        path = "C:\\Users\\Michelle\\OneDrive\\Documents\\Uni\\MRes\\Git_class\\weather-fun\\"
    return path

path = folder_path("work")
df = pd.read_csv("{}weather-raw.csv".format(path), header=None, index_col=0, names=data_labels)



# In[76]:

cols = []

for i in range(len(df.columns)):
    factor = re.findall("\d+", df.columns[i])
    col_name = df.columns[i]
    if factor:
        factor = int(factor[0])
        cols.append(col_name)
        var_name = re.split("_1", col_name)[0]
        df[var_name] = df[col_name] / factor
df.drop(columns=cols, inplace=True)

#%%
df.index = pd.to_datetime(df.index)


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

print(len(var_dict))
#%%
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


