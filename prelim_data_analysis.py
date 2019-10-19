
# coding: utf-8

# In[1]:


import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import glob
import re


# In[11]:


data_format = ["Timestamp (GMT)", "Temperature (Celcius * 10)", "Humidity (%)", "Dew Point (Celcius * 10)", 
               "Pressure (mBar)", "Mean wind speed (knots * 10)", "Average wind bearing (degrees)", "Sunshine (hours * 100)", 
               "Rainfall (mm * 1000)", "Max wind speed (knots * 10)]"]


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

path = folder_path("home")
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
# In[77]:
#df.drop("temp_10", axis=1, inplace=True)

df.columns


