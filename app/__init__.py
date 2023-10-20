import os

from flask import Flask
from app.controllers.college_controller import college_blueprint
from app.controllers.index_controller import index_blueprint
from app.models.college_model import CollegeModel 
from app.models.course_model import CourseModel 
from app.models.student_model import StudentModel

def create_app(connection):
    app = Flask(__name__)
    load_schema(connection)
    with app.app_context():
        app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
        app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
        app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
        app.config['MYSQL_DATABASE'] = os.getenv('MYSQL_DATABASE')
        app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

        app.register_blueprint(index_blueprint)
        app.register_blueprint(college_blueprint)

        return app

def load_schema(connection):  
    CollegeModel.create_table(connection)
    CourseModel.create_table(connection)
    StudentModel.create_table(connection)