# CSE-106 Lab_1 Q2
# Tyler Brittain

print('Pleas enter a sentence:')
sentence = input()
repeat = int(input('Please enter how many times it should be repeated: '))

with open('Lab_1/CompletedPunishment.txt', "w") as file:
    for i in range(0,repeat):
        file.write(sentence + "\n")