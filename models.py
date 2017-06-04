from flask.ext.sqlalchemy import SQLAlchemy
# from sqlalchemy import Column, String, Text, Boolean
# from Model import Model

db = SQLAlchemy()

class Task(db.Model):
	__tablename__ = 'tasks'
	uid = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
	title = db.Column(db.String(200), nullable=False)
	description = db.Column(db.Text, nullable=False)
	done = db.Column(db.Boolean, default=False)

	def __init__(self, title, description):
		self.title = title
		self.description = description

class MethodRewriteMiddleware(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        if 'METHOD_OVERRIDE' in environ.get('QUERY_STRING', ''):
            args = url_decode(environ['QUERY_STRING'])
            method = args.get('__METHOD_OVERRIDE__')
            if method:
                method = method.encode('ascii', 'replace')
                environ['REQUEST_METHOD'] = method
        return self.app(environ, start_response)