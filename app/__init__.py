import os
import cloudinary

from flask import Flask, session
from app.controllers.index_controller import index_blueprint
from app.controllers.college_controller import college_blueprint
from app.controllers.course_controller import course_blueprint
from app.controllers.student_controller import student_blueprint
from app.models.college_model import CollegeModel 
from app.models.course_model import CourseModel 
from app.models.student_model import StudentModel

def create_app(connection):
    app = Flask(__name__)
    app.secret_key = os.getenv('APP_SECRET')

    load_schema(connection)
    load_cloudinary()
    with app.app_context():
        app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
        app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
        app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
        app.config['MYSQL_DATABASE'] = os.getenv('MYSQL_DATABASE')
        app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
        app.config["SESSION_PERMANENT"] = False
        app.config["SESSION_TYPE"] = "filesystem"

        app.register_blueprint(index_blueprint)
        app.register_blueprint(college_blueprint)
        app.register_blueprint(course_blueprint)
        app.register_blueprint(student_blueprint)

        return app

def load_schema(connection):  
    CollegeModel.create_table(connection)
    CourseModel.create_table(connection)
    StudentModel.create_table(connection)

def load_cloudinary():
    cloudinary.config(
        cloud_name = os.getenv('CLOUD_NAME'),
        api_key = os.getenv('CLOUD_KEY'),
        api_secret = os.getenv('CLOUD_SECRET')
    )
