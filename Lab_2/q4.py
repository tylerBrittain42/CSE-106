#Go back and fix env/interpreter stuff

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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