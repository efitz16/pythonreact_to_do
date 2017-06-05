# from middleware import initialize_database as init_db
# from middleware import fill_database as fill_db
# from middleware import build_message
from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import db, Task
# , MethodRewriteMiddleware
from forms import TaskForm
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/pyflasktodo'
ma = Marshmallow(app)
db.init_app(app)

class TaskSchema(ma.Schema):
    class Meta:
        model = Task

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

app.secret_key = "developement-key"

@app.route("/")
def index():
	tasks = Task.query.all()
	return render_template("layout.html", tasks=tasks)

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/tasks/<id>", methods=['GET'])
def show(id):
	task = Task.query.get(id)
	return render_template("show.html", task=task)

@app.route("/tasks/<id>", methods=['PATCH'])
def edit(id):
	task = Task.query.get(id)
	task.done = True
	db.session.commit()
	return redirect(url_for('index'), code=302)

# @app.route("/tasks/<id>", methods=['DELETE'])
@app.route("/delete/tasks/<id>", methods=['POST'])
def delete(id):
	# return render_template("about.html")
	task = Task.query.get(id)
	db.session.delete(task)
	db.session.commit()
	return redirect(url_for('index'), code=302)

@app.route("/new/tasks", methods=['GET'])
def new():
	form = TaskForm()
	return render_template('newtask.html', form=form)

@app.route("/tasks", methods=['GET', 'POST'])
def create():
	form = TaskForm()
	if request.method == 'POST':
		newtask = Task(form.title.data, form.description.data)
		db.session.add(newtask)
		db.session.commit()
		return "Success!"
	elif request.method == 'GET':
		tasks = Task.query.all()
		# return render_template("layout.html", tasks=tasks)
		return jsonify({'tasks': tasks_schema.dump(tasks).data})	

if __name__ == "__main__":
	app.run(debug=True)

# def init_api_routes(app):
#     if app:
#     	app.add_url_rule('/tasks/<string:id>', 'task_by_id', task_by_id, methods=['GET'])
#         app.add_url_rule('/tasks', 'task', task, methods=['GET'])
#         app.add_url_rule('/tasks', 'add_task', methods=['POST'])
#         app.add_url_rule('/tasks/<string:id>', 'update_task', update_task, methods=['PUT'])
#         app.add_url_rule('/tasks/<string:id>', 'delete_task', delete_task, methods=['DELETE'])