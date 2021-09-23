import numpy as np
from numpy import linalg

# creates a numpy matrix from user input
def inputArr():

    row_count = int(input('# of rows: '))
    column_count = int(input('# of columns: '))
    non_num = []

    for cur_row in range(row_count):
        row = []
        for cur_col in range(column_count):
            row.append(int(input('ele: ')))
        non_num.append(row)

    arr = np.array(non_num)
    return arr

        
userInput = False

if(userInput == False):
    A = np.array([[1,2,3],[4,5,6],[7,8,9]])
    B = np.array([[3,1,4],[2,6,1],[2,9,7]])
else:
    print('Creating Matrix A')
    A = inputArr()
    print('Creating Matrix B')
    B = inputArr()
print("\n---Matrix A---")
print(A)
print("\n---Matrix B---")
print(B)

# Q1
try:
    print("\n---Question One---")
    matrix_sum = A + B
    print(matrix_sum)
except Exception as e:
    print(f'Error:{e}')

# Q2
try:
    print("\n---Question Two---")
    matrix_mult = A @ B
    print(matrix_mult)
except Exception as e:
    print(f'Error:{e}')


# Q3
try:
    print("\n---Question Three---")
    A_determinate = linalg.det(A)
    print(A_determinate)
except Exception as e:
    print(f'Error:{e}')

# Q4
try:
    print("\n---Question Four---")
    B_inverse = linalg.inv(B)
    print(B_inverse)
except Exception as e:
    print(f'Error:{e}')


# Q5
try:
    print("\n---Question Five---")
    A_eigen = linalg.eigvals(A)
    print(A_eigen)
except Exception as e:
    print(f'Error:{e}')
