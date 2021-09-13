count = 0
word = input("Please enter a word: ").lower()
with open("PythonSummary.txt", "r") as file:
    line = file.readline()
    while line:
        curLine = line.lower().split(' ')
        for i in curLine:
            count += i.count(word)
        line = file.readline()
print("The word {} appears {} times.".format(word, count))