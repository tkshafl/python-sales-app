from flask import Flask, render_template, request
from app import app
from app import db
from models.courses import Course

@app.route('/courses')
def courses():
    course_recs = db.session.query(Course).all() 
    courses = list(map(lambda rec: rec.__dict__, course_recs))
    return render_template('courses.html', courses = courses)

@app.route('/course',methods=['get'])
def course():
    id = request.args.get('id')
    course = Course.query.get(id)     
    return render_template('course_detail.html', course = course)