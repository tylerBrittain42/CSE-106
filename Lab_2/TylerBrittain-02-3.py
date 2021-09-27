import numpy as np
import pandas as pd

weather_frame = pd.read_csv("/home/tyler/Documents/Fall_2021/106_labs/Lab_2/weather_data.txt")

# Q1
precip = weather_frame.loc[:,["date","actual_precipitation"]]
precip = precip.loc[precip["actual_precipitation"] == precip["actual_precipitation"].max()]
print("\n---Question One---")
print('Days with highest actual percentage')
print(precip)

# Q2
actual_max_series = weather_frame.loc[(pd.to_datetime(weather_frame['date']) >= '2014-07-01') & (pd.to_datetime(weather_frame['date']) <= '2014-07-31'),"actual_max_temp"]
print("\n---Question Two---")
print(f'The average actual max temp in July 2014 is {actual_max_series.mean()}')

# Q3
q33 = weather_frame.loc[weather_frame["actual_max_temp"] == weather_frame["actual_max_temp"].max(),'date']
print("\n---Question Three---")
print('Days where the actual max temp is the record max temp')
print(q33)

# Q4
oct_rain = weather_frame.loc[(pd.to_datetime(weather_frame['date']) >= '2014-10-01') & (pd.to_datetime(weather_frame['date']) <= '2014-10-31'),"actual_precipitation"]
print("\n---Question Four---")
print(f'The sum of October 2014 rainfall is {oct_rain.sum()}')

# Q5
temp_range = weather_frame.loc[((weather_frame['actual_min_temp']) < 60) & (weather_frame['actual_max_temp'] > 90),"date" ]
print("\n---Question Five---")
print('Days where the actual low temperature is below 60 degrees and actual max temperature is above 90 degrees')
print(temp_range)
