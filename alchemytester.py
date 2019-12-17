from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, flash, redirect
#from forms import RegistrationForm, LoginForm
import sqlite3

app = Flask(__name__)

app.config['SECRET KEY'] = ''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
conn = sqlite3.connect("site.db")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS User ([id] INTEGER PRIMARY KEY AUTOINCREMENT)""")

conn.commit()
conn.close()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"

    posts = [
        {
            'author': 'Corey Schafer',
            'title': 'Blog Post 1',
            'content': 'First post content',
            'date_posted': 'April 20, 2018'
        },
        {
            'author': 'Jane Doe',
            'title': 'Blog Post 2',
            'content': 'Second post content',
            'date_posted': 'April 21, 2018'
        }
    ]


if __name__ == "__main__":
    app.run(debug=True)
