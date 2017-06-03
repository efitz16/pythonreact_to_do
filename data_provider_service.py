from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from Models import Task
from Models import init_database



class DataProviderService:
    def __init__(self, engine):
        if not engine:
            raise ValueError('The values specified in engine parameter has to be supported by SQLAlchemy')
        self.engine = engine
        db_engine = create_engine(engine)
        db_session = sessionmaker(bind=db_engine)
        self.session = db_session()

    def init_database(self):
        """
        Initializes the database tables and relationships
        :return: None
        """
        init_database(self.engine)

    def add_task(self, title, description):
        """
        Creates and saves a new candidate to the database.

        :param first_name: First Name of the candidate
        :param last_name: Last Name of the candidate
        :param email: Email address of the candidate
        :param birthday: Birthday of the candidate
        :param phone: Telephone number of the candidate
        :param languages: Language skills of the candidate
        :param skills: Skills which the candidate has
        :return: The id of the new Candidate
        """

        new_task = Task(title=title,
                        description=description)

        self.session.add(new_task)
        self.session.commit()

        return new_task.id

    def get_task(self, id=None, serialize=False):

        all_tasks = []

        if id is None:
            all_tasks = self.session.query(Task).order_by(Task.last_name).all()
        else:
            all_tasks = self.session.query(Task).filter(Task.id == id).all()

        if serialize:
            return [t.serialize() for t in all_tasks]
        else:
            return all_tasks

    def delete_task(self, id):
        if id:
            items_deleted = self.session.query(Task).filter(Task.id == id).delete()
            return items_deleted > 0
        return False
