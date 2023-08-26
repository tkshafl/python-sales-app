from flask import Flask, render_template, request
from app import app
from app import db
from models.users import User

@app.route('/users')
def users():
    user_recs = db.session.query(User).all()
    users = list(map(lambda rec: rec.__dict__, user_recs))
    return render_template('users.html', users = users)

# @app.route('/user/<int:id>',methods=['get'])
# def user(id):
#     user = User.query.get(id)     
#     return render_template('user_detail.html', user = users)

@app.route('/user',methods=['get'])
def user():
    id = request.args.get('id')
    user = User.query.get(id)     
    return render_template('user_detail.html', user = user)