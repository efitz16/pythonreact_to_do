from flask_wtf import Form
from wtforms import StringField, TextField

class TaskForm(Form):
	title = StringField('title')
	description = TextField('description')