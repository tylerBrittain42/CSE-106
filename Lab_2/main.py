#Go back and fix env/interpreter stuff

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Q 1.1
q1 = np.arange(2,10).reshape(4,2)
# print(q1)


# COME BACK TO THIS ONE
# Q 1.2
# # q2 = np.zeros((8,8))
q2 = np.zeros((8,8))
q2[::, ::2] = 1
# print(q2)


# Q 1.3
q3 = np.unique([10, 20, 10, 30, 20, 40, 20, 20, 10, 30, 0, 50, 10])
# print(q3)

# Q 1.4
q4 = np.array([6, 75, 9, 82, 36, 42, 59, 3, 52, 1, 32, 68, 93, 4, 27, 85, 0, -3, 57])
# print(q4[q4 > 37])

# Q 1.5 
q5 = np.array([0, 12, 45.21 ,34, 99.91])
q5 = q5 * (9/5) + 32
# print(q5)

# Q 2.1

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


# # Q 4.1

four_one = weather_frame.loc()[:,["date","actual_min_temp","actual_max_temp"]]
print(type(four_one))
# four_one.plot(x="date",y=["actual_min_temp","actual_max_temp"],color=['blue','red'],title="Min vs. Max temps",legend=['aaa','bbb'],ylabel="Temperature")
# plt.show()
# print('plotted')    

# # Q 4.2
# four_two = weather_frame.loc()[:,["actual_precipitation"]]
# # print(four_two)
# four_two.plot.hist(title="Precipitation").set_xlabel("precipation level(inches)")
# plt.show()