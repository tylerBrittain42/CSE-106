from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# NOTE: using a temporary grades object
# have not used error handling yet
grades = {'Tyler':100,'Steve':40}


@app.route('/')
def hello_world():
    return "<h1> Index </h1>"



# GET and POST /grades
@app.route('/grades', methods=["GET","POST"])
def grade_stuff(): 
    if request.method == 'GET':
        return grades
    elif request.method == 'POST':
        content = request.get_json(force=True)
        grades[content['name']] = content['grade']
        print(grades)
        return('Grade post recieved')


# GET /grades/<Student name>
@app.route('/grades/<name>')
def student_grade(name):
    return {name : grades[name]}


# PUT /grades/<Student Name>
@app.route('/grades/<name>', methods=["PUT"])
def put_student(name):
    content = request.get_json(force=True)
    grades[name] = content['grade']
    print(grades)
    return(f"PUT for {name} recieved")

# DELETE /grades/<Student Name>
@app.route('/grades/<name>', methods=["DELETE"])
def delete_student(name):
    del grades[name]
    return(f"DELETE for {name} recieved")