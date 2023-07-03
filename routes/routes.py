from flask import request, render_template
from connect_db import db
import re
from __main__ import app

def validateData(data):
    if len(data['name'].strip()) == 0:
        return False
    if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', data['email']):
        return False
    if len(data['college'].strip()) == 0:
        return False
    if len(data['start'].strip()) == 0:
        return False
    if len(data['end'].strip()) == 0:
        return False
    
    return True

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        if not validateData(request.form):
            return render_template('home.html', message = "Please enter valid data!")

        # get the data from form
        name = request.form['name']
        email = request.form['email']
        college = request.form['college']
        start = request.form['start']
        end = request.form['end']

        # insert into database
        student_collection = db['students']
        document = {'name':name, 'email':email, 'college':college, 'start':start, 'end':end} 
        result = student_collection.insert_one(document) 
        
        return render_template('home.html', message = "Submission successful!")
    
    if(request.method == "GET"):
        return render_template('home.html')
    

@app.get("/students")
def showStudents():
    students =  db['students'].find()
    return render_template('students.html', students=students)

