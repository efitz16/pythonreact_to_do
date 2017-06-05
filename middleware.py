from flask import jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for

from data_provider_service import DataProviderService

db_engine = 'mysql+mysqldb://packtuser:secret@localhost/packtwebapi?unix_socket=/opt/lampp/var/mysql/mysql.sock'


DATA_PROVIDER = DataProviderService(db_engine)

def add_task:
    title = request.form["title"]
    description = request.form["description"]

    new_task_id = DATA_PROVIDER.add_candidate(title=title, description=description)

    return return jsonify({
      "id": new_task_id
    })

def delete_task(id):
    if DATA_PROVIDER.delete_task(id):
        return make_response('', 204)
    else:
        return make_response('', 404)

def task(serialize = True):
    tasks = DATA_PROVIDER.get_task(serialize=serialize)
    if serialize:
        return jsonify({"tasks": tasks, "total": len(tasks)})
    else:
        return tasks


def task_by_id(id):
    current_task = DATA_PROVIDER.get_task(id, serialize=True)
    if current_task:
        return jsonify({"task": current_task})
    else:
        abort(404)

def update_task(id):
    new_task = {
        "done":request.form["done"]
    }
    updated_task = DATA_PROVIDER.update_task(id, new_task)
    if not updated_task:
        return make_response('', 204)
    else:
        return jsonify({"task": updated_task})


def initialize_database():
    DATA_PROVIDER.init_database()


def fill_database():
    DATA_PROVIDER.fill_database()

def build_message(key, message):
    return {key:message}