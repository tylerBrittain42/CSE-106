class course:

    def __init__(self,number, department,id,name,credits,days,start,end,avg):
        self.number = number
        self.department = department
        self.id = id
        self.number = number
        self.name = name
        self.credits = credits
        self.days = days
        self.start = start
        self.end = end
        self.avg = avg

    def printSummary(self):
        print(f"Course {self.number}: {self.id}: {self.name}")
        print(f"Number of Credits: {self.credits}")
        print(f"Days of Lectures: {self.days}")
        print(f"Lecture Time: {self.start} - {self.end}")
        print(f"Stat: on average, students get {self.avg}% in this course")

courses = []

with open("classesInput.txt", "r") as file:
    line = file.readline()
    total_classes = int(line)
    cur_class = 0

    while cur_class < total_classes:
        line = file.readline()
        department = line.strip()
        line = file.readline()
        id = line.strip()
        line = file.readline()
        name = line.strip()
        line = file.readline()
        credits = line.strip()
        line = file.readline()
        days = line.strip()
        line = file.readline()
        start = line.strip()
        line = file.readline()
        end = line.strip()
        line = file.readline()
        avg = line.strip()
        
        courses.append(course(cur_class + 1,department,id,name,credits,days,start,end,avg))
        cur_class += 1
for i in courses:
    i.printSummary()
    print()