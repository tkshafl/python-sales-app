from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
app = Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db.init_app(app)

from models.users import User
@app.route('/')
def hello_world():
    # rec = db.get_or_404(User,1)
    rec = User.query.get_or_404(1)
    return render_template('index.html', user=rec)

@app.route('/users')
def users():
    users = [{'id':1, 'first_name':'Tushar', 'last_name' :'Sha', 'username': 'Tusharksha' , 'email':'tusharksha@gmail.com' },
        {'id':2, 'first_name':'Mickey', 'last_name' :'mouse', 'username': 'MickeyMouse' , 'email':'Mickey@gmail.com' },
        {'id':3, 'first_name':'Jayashree', 'last_name':'Sha', 'username': 'Jayashreesha' , 'email':'sha.jayashree@gmail.com' }]
    return render_template('users.html', users = users)