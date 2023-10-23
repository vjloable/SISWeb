from flask import g
from app.services.database_service import DatabaseService
from mysql.connector import Error as MySQLError

class CollegeModel:

    #Create
    @staticmethod
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
            return {'success':True, 'response':"Inserted {}, {} into Colleges table successfuly".format(code, name)}
        except MySQLError as e:
            return {'success':False, 'response':str(e)}
        finally:
            cursor.close()
            connection.close()
    
    #Read
    @staticmethod
    def read(self, code):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            SELECT * FROM Colleges 
            WHERE code = '{}';
            """.format(str(code))
            )
            response = []
            data = cursor.fetchone()
            if data is not None:
                
                response = data
            connection.commit()
            return {'success':True, 'response':response}
        except MySQLError as e:
            return {'success':False, 'response':str(e)}
        finally:
            cursor.close()
            connection.close()

    #Update
    @staticmethod
    def update(self, code, name, new_code, new_name):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            UPDATE Colleges SET code = '{}', name = '{}' WHERE code = '{}';
            """.format(new_code, new_name, code)
            )
            connection.commit()
            return {'success':True, 'response':"Updated {}, {} with {}, {} into Colleges table successfuly".format(code, name, new_code, new_name)}
        except MySQLError as e:
            return {'success':False, 'response':str(e)}
        finally:
            cursor.close()
            connection.close()
    
    #Delete
    @staticmethod
    def delete(self, code):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            DELETE FROM Colleges WHERE code = '{}';
            """.format(code)
            )
            connection.commit()
            return {'success':True, 'response':"Deleted {} from Colleges table successfuly".format(code)}
        except MySQLError as e:
            return {'success':False, 'response':str(e)}
        finally:
            cursor.close()
            connection.close()

    #List
    @staticmethod
    def list_all(self):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            SELECT * FROM Colleges;
            """)
            response = cursor.fetchall()
            connection.commit()
            return {'success':True, 'response':response}
        except MySQLError as e:
            return {'success':False, 'response':str(e)}
        finally:
            cursor.close()
            connection.close()

    #Count
    @staticmethod
    def count_rows(self):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            SELECT COUNT(*) FROM Colleges;
            """)
            response = cursor.fetchone()[0]
            connection.commit()
            return {'success':True, 'response':int(response)}
        except MySQLError as e:
            return {'success':False, 'response':str(e)}
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