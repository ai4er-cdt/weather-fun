#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 15:18:31 2019

@author: mwlw3
"""

import pandas
import os
import re
from helper_functions import save_csv_from_url

url = "https://www.cl.cam.ac.uk/research/dtg/weather/weather-raw.csv"
data_file = "data.csv"

if not os.path.exists(data_file):
	save_csv_from_url(url, data_file)

data_labels = ["time", "temp_10", "humidity", "dew_point_10", 
               "pressure", "mean_wind_speed_10", "avg_wind_bearing", "sunshine_100", 
               "rainfall_1000", "max_wind_speed_10"]
    
df = pandas.read_csv(data_file,header=None, index_col=0, names=data_labels)


def column_factors(df):
    """ Divides specific columns of data by the factor specified in the column name. """
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

column_factors(df)
df.index = pandas.to_datetime(df.index)

df.to_csv("data_tidy.csv")