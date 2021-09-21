#Go back and fix env/interpreter stuff

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# Question 3

weather_frame = pd.read_csv("/home/tyler/Documents/Fall_2021/106_labs/Lab_2/weather_data.txt")

# Q 3.1
precip = weather_frame.loc[:,["date","actual_precipitation"]]
precip = precip.loc[precip["actual_precipitation"] == precip["actual_precipitation"].max()]
# print(precip)

# Q 3.2
# df[(df['date'] > '2013-01-01') & (df['date'] < '2013-02-01')]
# actual_max_temp
actual_max_series = weather_frame.loc[(pd.to_datetime(weather_frame['date']) >= '2014-07-01') & (pd.to_datetime(weather_frame['date']) <= '2014-07-31'),"actual_max_temp"]
# print(actual_max_series.mean())

# Q 3.3
q33 = weather_frame.loc[weather_frame["actual_max_temp"] == weather_frame["actual_max_temp"].max(),'date']
# print(q33)

# Q3.4
oct_rain = weather_frame.loc[(pd.to_datetime(weather_frame['date']) >= '2014-07-01') & (pd.to_datetime(weather_frame['date']) <= '2014-07-31'),"actual_precipitation"]
# print(oct_rain.sum())

# Q 3.5
temp_range = weather_frame.loc[((weather_frame['actual_min_temp']) < 60) & (weather_frame['actual_max_temp'] > 90),"date" ]
# print(temp_range)
