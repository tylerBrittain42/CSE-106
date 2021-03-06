# from os import abort
from flask import Flask, request, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///grades.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Grade(db.Model):
    name = db.Column(db.String, primary_key=True)
    grade = db.Column(db.String)

    def json(self):
        return {self.name : self.grade}

    def __repr__(self):
        return f'{self.name} : {self.grade}'



@app.route('/')
def index():
    return "<h1> Index </h1>"



# GET and POST /grades
@app.route('/grades', methods=["GET","POST"])
def grade_stuff(): 
    if request.method == 'GET':
        gradess = Grade.query.all()
        return listToDict(gradess)
        
    elif request.method == 'POST':
        content = request.get_json()
        if Grade.query.filter_by(name=content['name']).first() is not None:
            abort(409)
        new_user = Grade(name=content['name'],grade=content['grade'])
        db.session.add(new_user)
        db.session.commit()
        return('Grade post recieved')


# GET /grades/<Student name>
@app.route('/grades/<stu_name>')
def student_grade(stu_name):
    res = Grade.query.filter_by(name=stu_name).first()
    if res is None:
        abort(404)
    return {res.name:res.grade}


# PUT /grades/<Student Name>
@app.route('/grades/<stu_name>', methods=["PUT"])
def put_student(stu_name):
    content = request.get_json()

    res = Grade.query.filter_by(name=stu_name).first()
    if res is None:
        abort(404)
    res.grade = content['grade']
    db.session.commit()

    return(f"PUT for {stu_name} recieved")

# DELETE /grades/<Student Name>
@app.route('/grades/<stu_name>', methods=["DELETE"])
def delete_student(stu_name):

    res = Grade.query.filter_by(name=stu_name).first()
    if res is None:
        abort(404)
    db.session.delete(res)
    db.session.commit()

    return(f"DELETE for {stu_name} recieved") 


@app.route('/reset')
def reset_db():

    # Deleting everything in table
    db.session.query(Grade).delete()

    # Adding new users to table
    steve = Grade(name='steve',grade='69')
    db.session.add(steve)

    phil = Grade(name='philly',grade='100')
    db.session.add(phil)

    tyler = Grade(name='tyler',grade='42a')
    db.session.add(tyler)



    db.session.commit()
    return '<h1> reset triggered </h1>'


def listToDict(llist):
    dictt = {}
    for ele in llist:
        dictt[ele.name] = ele.grade
    return dictt