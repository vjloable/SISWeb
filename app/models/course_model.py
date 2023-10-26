from flask import g
from app.services.database_service import DatabaseService
from mysql.connector import Error as MySQLError

class CourseModel:

    #Create
    @staticmethod
    def insert(code, name, college_code):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            INSERT INTO Courses
            VALUES ("{}", "{}", "{}");
            """.format(code, name, college_code)
            )
            connection.commit()
            return {'success':True, 'results':"Inserted {}, {}, {} into Courses table successfuly".format(code, name, college_code)}
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
            SELECT * FROM Courses 
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
    def update(code, new_code, new_name, new_college_code):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            UPDATE Courses SET Code = '{}', Name = '{}', College = '{}' WHERE Code = '{}';
            """.format(new_code, new_name, new_college_code, code)
            )
            connection.commit()
            return {'success':True, 'results':"Updated {} into Courses table successfuly".format(code)}
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
            DELETE FROM Courses WHERE Code = '{}';
            """.format(code)
            )
            connection.commit()
            return {'success':True, 'results':"Deleted {} from Courses table successfuly".format(code)}
        except MySQLError as e:
            return {'success':False, 'results':str(e)}
        finally:
            cursor.close()
            connection.close()

    #List
    @staticmethod
    def list_all(query=None):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            if query is None:
                cursor.execute("""
                SELECT * FROM Courses;
                """)
                results = list(cursor.fetchall())
                connection.commit()
                return {'success':True, 'results':results}
            else:
                cursor.execute("""
                SELECT * FROM Courses 
                WHERE Code LIKE '%{}%' OR Name LIKE '%{}%' OR College LIKE '%{}%';
                """.format(query, query, query))
                results_raw = list(cursor.fetchall())
                results = []
                for result in results_raw:
                    results.append({"name"  : str(result[1]), "value" : str(result[0])})
                success = len(results) > 0
                connection.commit()
                return {'success':success, 'results':results}
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
            SELECT COUNT(*) FROM Courses;
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
        CREATE TABLE IF NOT EXISTS Courses(
            Code char(20) NOT NULL,
            Name char(150) NOT NULL,
            College char(20),
            PRIMARY KEY (Code),
            FOREIGN KEY (College) REFERENCES Colleges(Code) ON DELETE CASCADE
        );
        """)