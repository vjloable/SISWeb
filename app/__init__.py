import os

from flask import Flask
from app.services.database_service import DatabaseService

def create_app():
    app = Flask(__name__)
    
    app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
    app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
    app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
    app.config['MYSQL_DATABASE'] = os.getenv('MYSQL_DATABASE')
    
    database_service = DatabaseService()
    app.teardown_appcontext(database_service.close)
    
    # from app.controllers import <module>
    # app.register_blueprint(<module>)

    return app