class TooShort(Exception):
    """Raised when not enough entries"""
    pass

sum = 0

numbers = input("Please enter a series of numbers separated by spaces: ")
num_list = numbers.split(" ")

try:
    if(len(num_list) < 2):
        raise TooShort
    for i in num_list:
        sum += float(i)
    print(f'{sum}')
except(ValueError):
    print("Error: non int value detected")
except(TooShort):
    print("Error: not enough entries")



