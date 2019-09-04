from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///richMenu.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class RichMenu(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	content = db.Column(db.String(100))
	name    = db.Column(db.String(50))

	def __init__(self, name, content):
		self.content = content
		self.name    = name
	def __depr__(self):
		return '<richMenu %r>' % self.content
