from flask import g
from app.services.database_service import DatabaseService
from mysql.connector import Error as MySQLError

class CollegeModel:

    #Create
    def insert(self, code, name):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            INSERT INTO Colleges
            VALUES ("{}", "{}");
            """.format(code, name)
            )
            connection.commit()
            return {'success':'true', "response":"Inserted {}, {} into Colleges table successfuly".format(code, name)}
        except MySQLError as e:
            return {'success':'false', 'response':str(e)}
        finally:
            cursor.close()
            connection.close()

    #List
    def list_all(self):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            SELECT * FROM Colleges;
            """)
            response = cursor.fetchall()
            connection.commit()
            return {'success':'true', "response":response}
        except MySQLError as e:
            return {'success':'false', 'response':str(e)}
        finally:
            cursor.close()
            connection.close()

    #Count
    def count_rows(self):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            SELECT COUNT(*) FROM Colleges;
            """)
            response = cursor.fetchone()[0]
            connection.commit()
            return {'success':'true', "response":int(response)}
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