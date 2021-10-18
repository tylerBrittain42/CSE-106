from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1> Index </h1>"



# GET /grades
@app.route('/grades')
def all_grades():
    return "GOT grades"
    

# GET /grades/<Student name>
@app.route('/grades/<name>')
def student_grade(name):
    return f"GOT {name}'s grades"


# POST /grades
@app.route('/grades', methods=["POST"])
def add_student():
    return('Grade post recieved')


# PUT /grades/<Student Name>
@app.route('/grades/<name>', methods=["PUT"])
def put_student(name):
    return(f"PUT for {name} recieved")