from createDBInstance import db

class RichMenu(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	content = db.Column(db.String(100))
	name    = db.Column(db.String(50))

	def __init__(self, content):
		self.content = content
	def __depr__(self):
		return '<richMenu %r>' % self.content