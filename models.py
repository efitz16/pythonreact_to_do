from flask.ext.sqlalchemy import SQLAlchemy
# from sqlalchemy import Column, String, Text, Boolean
# from Model import Model

db = SQLAlchemy()

class User(db.Model):
	__tablename__ = 'tasks'
	uid = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
	title = db.Column(db.String(200), nullable=False)
	description = db.Column(db.Text, nullable=False)
	done = db.Column(db.Boolean, default=False)

	def __init__(self, title, description, done):
		self.title = title
		self.description = description
		self.done = done

	@property
	def id(self):
		return self.id

	@property
	def title(self):
		return self.title

	@title.setter
	def title(self, value):
		self.__title = value

	@property
	def description(self):
		return self.description

	@description.setter
	def description(self, value):
		self.__description = value

	@property
	def done(self):
		return self.done

	@done.setter
	def done(self, value):
		self.__done = value

	def serialize(self):
		return {
			"id": self.id,
			"title": self.title,
			"description": self.description,
			"done": self.done
		}
