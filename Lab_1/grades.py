# CSE-106 Lab_1 Q5
# Tyler Brittain

import json

'''
5) Create a grades program that does the following (25 points):
a. Allows a user to create a student name and grade
b. Allows a user to ask for a grade, given the full name of the student
c. Allows a user to edit a grade
d. Allows a user to delete a grade
e. Reads/writes to grades.txt to store grade data persistently in JSON format
f. Stores grades in memory data as a dictionary and updates grades.txt with any changes
g. Loads grade data from grades.txt into dictionary on program start up
'''

def displayOptions():
    print("Please Select an option")
    print("1) Create a student")
    print("2) Get a Student's Grade")
    print("3) Edit a grade")
    print("4) delete a grade")
    print("5) Exit")


with open('Lab_1/grades.txt',"r") as file:
    grades = json.load(file)

option = None

while(option != 5):
    displayOptions()
    option = int(input("Options:"))
    print()
    
    # add a student
    if(option == 1):
        print("Adding Student")
        student = input("Name: ")
        grade = input("Grade: ")
        grades[student] = grade
    
    # get student grade
    elif(option == 2):
        print("Get student grade")
        student = input('Student name:')
        print(f"{student} has a grade {grades[student]}")

    # edit student grade
    elif(option == 3):
        print("Edit grade")
        student = input("Student: ")
        grade = input("New Grade: ")
        grades[student] = grade

    # delete student grade
    elif(option == 4):
        print("Delete Grade")
        student = input("Student: ")
        del(grades[student])
    print()
    print()

    with open("Lab_1/grades.txt", "w") as outfile:
        json.dump(grades,outfile)
