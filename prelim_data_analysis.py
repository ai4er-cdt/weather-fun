
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


df = pd.read_csv("/home/mwlw3/Documents/Git_class/weather-fun/weather-raw.csv", header=None, index_col=0, names=data_labels)


# In[74]:


df


# In[62]:


df['temp'] = df['temp_10'] / 10


# In[76]:


for i in range(len(df.columns)):
    factor = re.findall("\d+", df.columns[i])
    col_name = df.columns[i]
    if factor:
        factor = int(factor[0])
        df[col_name+"_new"] = df[col_name] / factor
        df.drop(labels=col_name, axis='columns')


# In[77]:


df


# In[46]:


name


# In[68]:


int(factor)

