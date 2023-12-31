from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import or_
from app import app
from app import db
from models.users import User

@app.route('/users')
def users():
    email_query = request.args.get('email')

    if email_query:
        user_recs = db.session.query(User).filter(or_(User.email.ilike(f'%{email_query.lower()}%'))).all()
    else:
        user_recs = db.session.query(User).all()

    users = list(map(lambda rec: rec.__dict__, user_recs))
    return render_template('users.html', users=users)

# @app.route('/user/<int:id>',methods=['get'])
# def user(id):
#     user = User.query.get(id)     
#     return render_template('user_detail.html', user = users)

@app.route('/user',methods=['GET','POST'])
def user():
    id = request.args.get('id')
    if request.method == "GET":
        if id:
            user = User.query.get(id)  
            form_action = request.args.get('action')
            if form_action=="Edit":
               return render_template('user_form.html', user=user) 
            elif form_action == 'Delete' :
                db.session.delete(user)
                db.session.commit()
                return redirect(url_for('users'))   
            else:
                return render_template('user_detail.html', user = user)
        else:
             return render_template('user_form.html', user=None)
    elif request.method == "POST":
        id = request.form['id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        email = request.form['email']
        if id:
            user = User.query.get(id)
            user.first_name = first_name
            user.last_name = last_name 
            user.username = username
            user.email = email            
        else:
            user = User (
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email
            )
            db.session.add(user)
        db.session.commit()
        return redirect(url_for('users'))         