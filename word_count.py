# Should there be 3 or 2
count = 0
word = input("Please enter a word: ").lower()
with open("PythonSummary.txt", "r") as file:
    line = file.readline()
    while line:
        curLine = line.lower().split(' ')
        for i in curLine:
            count += i.count(word)
        line = file.readline()
print(f"The word {word} appears {count} times.")