import numpy as np

'''
A) Yes, change val
B) Yes, change val
c) Yes, use bincount to count instances
d) yes, split on ' '
'''


# Q 1
q1 = np.arange(2,10).reshape(4,2)
print("---Question One---")
print(q1)


# Q 1.2
q2 = np.zeros((8,8))
q2[::2, ::2] = 1
q2[1::2, 1::2] = 1
print("\n---Question Two---")
print(q2)


# Q 1.3
q3 = np.unique([10, 20, 10, 30, 20, 40, 20, 20, 10, 30, 0, 50, 10])
q3_alt = set([10, 20, 10, 30, 20, 40, 20, 20, 10, 30, 0, 50, 10])
print("\n---Question Three---")
print(q3)
print('or with sets')
print(q3_alt)


# Q 1.4
print("\n---Question Four---")
q4 = np.array([6, 75, 9, 82, 36, 42, 59, 3, 52, 1, 32, 68, 93, 4, 27, 85, 0, -3, 57])
print(q4[q4 > 37])

# Q 1.5
print("\n---Question Five---") 
q5 = np.array([0, 12, 45.21 ,34, 99.91])
q5 = q5 * (9/5) + 32
print(q5)

