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
