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
    print(sum)
except(ValueError):
    print("Error: non int value detected")
except(TooShort):
    print("Error: not enough entries")



# if(any(type(entry) is (ord() for entry in num_list)):
#     print("String detected")


# for i in numbers.split(" "):
#     sum += int(i)
# print(sum)
# except():
# print(e)