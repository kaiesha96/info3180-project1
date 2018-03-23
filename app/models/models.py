from app import db
from time import time
from datetime import date
class Users(db.Model):
	__tablename__ = 'user_profiles'
	userid	        = db.Column(db.Integer, primary_key=True)
	email       	= db.Column(db.String)
	first_name  	= db.Column(db.String())
	last_name		= db.Column(db.String())
	gender  		= db.Column(db.String())
	photo			= db.Column(db.String())
	bio			  	= db.Column(db.String())
	location	  	= db.Column(db.String())
	date_created	= db.Column(db.String())
	def __init__(self, first_name, last_name, email, gender, photo, location, bio):
		self.userid 		= long(time())
		self.email		 	= email
		self.first_name 	= first_name
		self.last_name 		= last_name
		self.gender 		= gender
		self.photo  		= photo
		self.bio 			= bio
		self.location		= location
		self.date_created	= "{0:%A}, {0:%B} {0:%d}, 20{0:%y}".format(date.today())