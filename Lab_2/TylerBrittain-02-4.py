import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

weather_frame = pd.read_csv("/home/tyler/Documents/Fall_2021/106_labs/Lab_2/weather_data.txt")

# Q1
one = weather_frame.loc()[:,["date","actual_min_temp","actual_max_temp"]]
one.plot(x="date",y=["actual_min_temp","actual_max_temp"],color=['blue','red'],title="Min vs. Max temps",legend=['aaa','bbb'],ylabel="Temperature")

# Q2
two = weather_frame.loc()[:,["actual_precipitation"]]
two.plot.hist(title="Precipitation").set_xlabel("precipation level(inches)")
plt.show()