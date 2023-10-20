from flask import g
from app.services.database_service import DatabaseService
from mysql.connector import Error as MySQLError

class CollegeModel:
    def insert(self, code, name):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            INSERT INTO Colleges
            VALUES ("{}", "{}");
            """.format(code, name)
            )
            response = cursor.fetchall()
            return {'success':'true', "response":str(response)}
        except MySQLError as e:
            return {'success':'false', 'response':str(e)}
        finally:
            cursor.close()
            connection.close()

    def list_all(self):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            SELECT * FROM Colleges;
            """)
            response = []
            row = cursor.fetchall()
            for data in row:
                response.append({"code":str(data[0]), "name":str(data[1])})
            return {'success':'true', "response":response}
        except MySQLError as e:
            return {'success':'false', 'response':str(e)}
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def create_table(connection):
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Colleges(
            Code char(20) NOT NULL,
            Name char(150) NOT NULL,
            PRIMARY KEY (Code)
        );
        """)