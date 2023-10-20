import mysql.connector
import os

from flask import g
from dotenv import load_dotenv
from app.models.college_model import CollegeModel 
from app.models.course_model import CourseModel 
from app.models.student_model import StudentModel 

load_dotenv()

class DatabaseService:
    def __init__(self):
        self.user = os.getenv('MYSQL_USER')
        self.password = os.getenv('MYSQL_PASSWORD')
        self.host = os.getenv('MYSQL_HOST')
        self.database = os.getenv('MYSQL_DATABASE')
        self.connection = None

        print("Initialize database")
    
    def __del__(self):
        self.close()
        print("Deleting database instance")

    def connect(self):
        if self.connection is None:
            connection = mysql.connector.connect(
                user = self.user,
                password = self.password,
                host = self.host,
                database = self.database
                )
            cursor = connection.cursor()
            self.create_tables(cursor)
            print("Connecting to database")
            self.connection = connection
        return self.connection
    
    @staticmethod
    def get_connection(self):
        return self.connection
    
    def close(self):
        print("Closing the database")
        if self.connection:
            self.connection.close()
            self.connection = None
    
    def create_tables(self, cursor):
        print("Creating tables")
        CollegeModel.create_table(cursor)
        CourseModel.create_table(cursor)
        StudentModel.create_table(cursor)