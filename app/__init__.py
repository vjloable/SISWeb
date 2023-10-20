import os

from flask import Flask
from app.controllers.college_controller import college_blueprint
from app.controllers.index_controller import index_blueprint

def create_app():
    app = Flask(__name__)
    
    app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
    app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
    app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
    app.config['MYSQL_DATABASE'] = os.getenv('MYSQL_DATABASE')

    app.register_blueprint(index_blueprint)
    app.register_blueprint(college_blueprint)

    return app