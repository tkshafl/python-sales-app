from flask import Flask, render_template
from app import app
from app import db
from models.users import User

@app.route('/users')
def users():
    user_recs = db.session.query(User).all()
    users = list(map(lambda rec: rec.__dict__, user_recs))
    return render_template('users.html', users = users)