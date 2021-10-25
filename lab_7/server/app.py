from os import abort
from flask import Flask, request, abort
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


# have not used error handling yet
# check error for when grades.txt empty

#implement success code(200) responses

with open('grades.txt',"r") as file:
    try:
        grades = json.load(file)
    except:
        grades = {}


@app.route('/')
def index():
    return "<h1> Index </h1>"



# GET and POST /grades
@app.route('/grades', methods=["GET","POST"])
def grade_stuff(): 
    if request.method == 'GET':
        return grades
    elif request.method == 'POST':
        content = request.get_json()
        if content['name'] in grades.keys():
            abort(409)
        grades[content['name']] = content['grade']
        with open("grades.txt", "w") as outfile:
            json.dump(grades,outfile)
        return('Grade post recieved')


# GET /grades/<Student name>
@app.route('/grades/<name>')
def student_grade(name):
    if name not in grades.keys():
        abort(404)
    return {name : grades[name]}


# PUT /grades/<Student Name>
@app.route('/grades/<name>', methods=["PUT"])
def put_student(name):
    content = request.get_json()
    if name not in grades.keys():
        abort(404)
    grades[name] = content['grade']
    with open("grades.txt", "w") as outfile:
        json.dump(grades,outfile)
    return(f"PUT for {name} recieved")

# DELETE /grades/<Student Name>
@app.route('/grades/<name>', methods=["DELETE"])
def delete_student(name):
    if name not in grades.keys():
        abort(404)
    del grades[name]
    with open("grades.txt", "w") as outfile:
        json.dump(grades,outfile)

    return(f"DELETE for {name} recieved") 