from flask import g
from app.services.database_service import DatabaseService
from mysql.connector import Error as MySQLError

class CollegeModel:

    #Create
    @staticmethod
    def insert(code, name):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            INSERT INTO Colleges
            VALUES ("{}", "{}");
            """.format(code, name)
            )
            connection.commit()
            return {'success':True, 'results':"Inserted ({}, {}) into Colleges table successfuly".format(code, name)}
        except MySQLError as e:
            return {'success':False, 'results':str(e)}
        finally:
            cursor.close()
            connection.close()
    
    #Read
    @staticmethod
    def read(code):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            SELECT * FROM Colleges 
            WHERE Code = '{}';
            """.format(str(code))
            )
            results = []
            data = cursor.fetchone()
            if data is not None:
                
                results = data
            connection.commit()
            return {'success':True, 'results':results}
        except MySQLError as e:
            return {'success':False, 'results':str(e)}
        finally:
            cursor.close()
            connection.close()

    #Update
    @staticmethod
    def update(code, new_code, new_name):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            UPDATE Colleges SET Code = '{}', Name = '{}' WHERE Code = '{}';
            """.format(new_code, new_name, code)
            )
            connection.commit()
            return {'success':True, 'results':"Updated {} into Colleges table successfuly".format(code)}
        except MySQLError as e:
            return {'success':False, 'results':str(e)}
        finally:
            cursor.close()
            connection.close()
    
    #Delete
    @staticmethod
    def delete(code):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            DELETE FROM Colleges WHERE Code = '{}';
            """.format(code)
            )
            connection.commit()
            return {'success':True, 'results':"Deleted {} from Colleges table successfuly".format(code)}
        except MySQLError as e:
            return {'success':False, 'results':str(e)}
        finally:
            cursor.close()
            connection.close()

    #List
    @staticmethod
    def list_all(formatted=false):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            SELECT * FROM Colleges;
            """)
            results = list(cursor.fetchall())
            connection.commit()
            # if formatted:
            #     results = 
            return {'success':True, 'results':results}
        except MySQLError as e:
            return {'success':False, 'results':str(e)}
        finally:
            cursor.close()
            connection.close()

    #Count
    @staticmethod
    def count_rows():
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            SELECT COUNT(*) FROM Colleges;
            """)
            results = cursor.fetchone()[0]
            connection.commit()
            return {'success':True, 'results':int(results)}
        except MySQLError as e:
            return {'success':False, 'results':str(e)}
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