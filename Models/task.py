import uuid
from sqlalchemy import Column, String, Text, Boolean
from Model import Model

class Task(Model):
	__tablename__ = 'tasks'
	id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
	title = Column(String(200), nullable=False)
	description = Column(Text, nullable=False)
	__done = Column(Boolean, default=False)

	def __init__(self, title, description, done):
		self.__id = uuid.uuid4()
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
