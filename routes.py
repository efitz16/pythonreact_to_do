# from middleware import initialize_database as init_db
# from middleware import fill_database as fill_db
# from middleware import build_message
from flask import Flask , render_template
from models import db
from forms import TaskForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://packtuser:secret@localhost/packtwebapi?unix_socket=/opt/lampp/var/mysql/mysql.sock'
db.init_app(app)

app.secret_key = "developement-key"

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/new/task")
def new_task():
	form = TaskForm()
	return render_template('newtask.html', form=form)

if __name__ == "__main__":
	app.run(debug=True)

# def init_api_routes(app):
#     if app:
#     	app.add_url_rule('/tasks/<string:id>', 'task_by_id', task_by_id, methods=['GET'])
#         app.add_url_rule('/tasks', 'task', task, methods=['GET'])
#         app.add_url_rule('/tasks', 'add_task', methods=['POST'])
#         app.add_url_rule('/tasks/<string:id>', 'update_task', update_task, methods=['PUT'])
#         app.add_url_rule('/tasks/<string:id>', 'delete_task', delete_task, methods=['DELETE'])