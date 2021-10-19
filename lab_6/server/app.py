from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return "<h1> Index </h1>"



# GET and POST /grades
@app.route('/grades', methods=["GET","POST"])
def grade_stuff():
    if request.method == 'GET':
        print(request)
        return "GOT grades"
    elif request.method == 'POST':
        return('Grade post recieved')


# GET /grades/<Student name>
@app.route('/grades/<name>')
def student_grade(name):
    return f"GOT {name}'s grades"


# PUT /grades/<Student Name>
@app.route('/grades/<name>', methods=["PUT"])
def put_student(name):
    return(f"PUT for {name} recieved")

# PUT /grades/<Student Name>
@app.route('/grades/<name>', methods=["DELETE"])
def delete_student(name):
    return(f"DELETE for {name} recieved")