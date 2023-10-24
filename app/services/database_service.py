import mysql.connector
import os

from flask import g
from dotenv import load_dotenv

load_dotenv()

class DatabaseService:
    def __init__(self):
        self.user = os.getenv('MYSQL_USER')
        self.password = os.getenv('MYSQL_PASSWORD')
        self.host = os.getenv('MYSQL_HOST')
        self.database = os.getenv('MYSQL_DATABASE')
        self.connection = None
        print("Initialize database")
    
    def connect(self):
        if self.connection is None:
            connection = mysql.connector.connect(
                user = self.user,
                password = self.password,
                host = self.host,
                database = self.database
                )
            self.connection = connection
            print("Connecting to database")
        return self.connection

    def close(self):
        print("Closing the database")
        if self.connection:
            self.connection.close()
            self.connection = None