from flask import g
from app.services.database_service import DatabaseService
from mysql.connector import Error as MySQLError

class StudentModel:

    #Create
    @staticmethod
    def insert(student_id, firstname, lastname, course_id, year, gender):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            INSERT INTO Students
            VALUES ("{}", "{}", "{}", "{}", "{}", "{}");
            """.format(student_id, firstname, lastname, course_id, year, gender)
            )
            connection.commit()
            return {'success':True, 'results':"Inserted {}, {}, {}, {}, {}, {} into Students table successfuly".format(student_id, firstname, lastname, course_id, year, gender)}
        except MySQLError as e:
            return {'success':False, 'results':str(e)}
        finally:
            cursor.close()
            connection.close()
    
    #Read
    @staticmethod
    def read(student_id):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            SELECT * FROM Students 
            WHERE ID = '{}';
            """.format(str(student_id))
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
    def update(student_id, new_student_id, new_firstname, new_lastname, new_course_id, new_year, new_gender):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            UPDATE Students SET ID = '{}', Firstname = '{}', Lastname = '{}', Course = '{}', Year = '{}', Gender = '{}' WHERE ID = '{}';
            """.format(new_student_id, new_firstname, new_lastname, new_course_id, new_year, new_gender, id)
            )
            connection.commit()
            return {'success':True, 'results':"Updated {} into Students table successfuly".format(student_id)}
        except MySQLError as e:
            return {'success':False, 'results':str(e)}
        finally:
            cursor.close()
            connection.close()
    
    #Delete
    @staticmethod
    def delete(student_id):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            DELETE FROM Students WHERE ID = '{}';
            """.format(student_id)
            )
            connection.commit()
            return {'success':True, 'results':"Deleted {} from Students table successfuly".format(id)}
        except MySQLError as e:
            return {'success':False, 'results':str(e)}
        finally:
            cursor.close()
            connection.close()

    #List
    @staticmethod
    def list_all():
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            SELECT * FROM Students;
            """)
            results = list(cursor.fetchall())
            connection.commit()
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
            SELECT COUNT(*) FROM Students;
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
        CREATE TABLE IF NOT EXISTS Students(
            ID char(9) NOT NULL,
            Firstname char(150) NOT NULL,
            Lastname char(150) NOT NULL, 
            Course char(20),
            Year enum('1st','2nd','3rd','4th') NOT NULL,
            Gender enum('Woman','Man','Transgender','Non-binary/Non-conforming','Prefer not to respond') NOT NULL,              
            PRIMARY KEY (ID),
            FOREIGN KEY (Course) REFERENCES Courses(Code) ON DELETE CASCADE
        );
        """)