from flask import g
from app.services.database_service import DatabaseService
from mysql.connector import Error as MySQLError

class StudentModel:

    #Create
    @staticmethod
    def insert(student_id, firstname, lastname, course, year, gender):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            INSERT INTO Students (StudentId, Firstname, Lastname, Course, Year, Gender)
            VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "");
            """.format(student_id, firstname, lastname, course, year, gender)
            )
            connection.commit()
            return {'success':True, 'results':"Inserted {}, {}, {}, {}, {}, {}. into Students table successfuly".format(student_id, firstname, lastname, course, year, gender)}
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
            SELECT Students.StudentId, Students.Firstname, Students.Lastname, Courses.Name, Students.Year, Students.Gender, Students.ImgURL FROM Students 
            LEFT JOIN Courses
            ON Students.Course = Courses.Code
            WHERE Students.StudentId = '{}';
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
            UPDATE Students SET StudentId = '{}', Firstname = '{}', Lastname = '{}', Course = '{}', Year = '{}', Gender = '{}' WHERE StudentId = '{}';
            """.format(new_student_id, new_firstname, new_lastname, new_course_id, new_year, new_gender, student_id)
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
            DELETE FROM Students WHERE StudentId = '{}';
            """.format(student_id)
            )
            connection.commit()
            return {'success':True, 'results':"Deleted {} from Students table successfuly".format(student_id)}
        except MySQLError as e:
            return {'success':False, 'results':str(e)}
        finally:
            cursor.close()
            connection.close()

    # List
    @staticmethod
    def get_list(offset, query="",):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            if offset >= 0:
                if query == "":
                    cursor.execute(f"""
                    SELECT Students.*, CollegeQuery.CollegeName FROM Students 
                    LEFT JOIN (
                        SELECT Colleges.Code AS CollegeCode, Colleges.Name AS CollegeName, Courses.College AS CourseCollege, Courses.Code AS CourseCode
                        FROM Colleges LEFT JOIN Courses ON Colleges.Code = Courses.College
                    ) AS CollegeQuery
                    ON Students.Course = CollegeQuery.CourseCode
                    LIMIT 11 
                    OFFSET {offset};
                    """)
                    results = list(cursor.fetchall())
                    connection.commit()
                    return {'success': True, 'results': results}
                else:
                    cursor.execute(f"""
                    SELECT Students.*, CollegeQuery.CollegeName FROM Students 
                    LEFT JOIN (
                        SELECT Colleges.Code AS CollegeCode, Colleges.Name AS CollegeName, Courses.College AS CourseCollege, Courses.Code AS CourseCode
                        FROM Colleges LEFT JOIN Courses ON Colleges.Code = Courses.College
                    ) AS CollegeQuery
                    ON Students.Course = CollegeQuery.CourseCode
                    WHERE Students.StudentId LIKE '%{query}%' 
                    OR Students.Firstname LIKE '%{query}%' 
                    OR Students.Lastname LIKE '%{query}%'
                    OR Students.Course LIKE '%{query}%' 
                    OR Students.Year LIKE '%{query}%' 
                    OR Students.Gender LIKE '%{query}%'
                    OR CollegeQuery.CollegeName LIKE '%{query}%' 
                    OR CollegeQuery.CollegeCode LIKE '%{query}%' 
                    LIMIT 11 
                    OFFSET {offset};
                    """);
                    results = list(cursor.fetchall())
                    success = len(results) > 0
                    connection.commit()
                    return {'success': success, 'results': results}
            else:
                cursor.execute(f"""
                SELECT Students.*, CollegeQuery.CollegeName FROM Students 
                LEFT JOIN (
                    SELECT Colleges.Code AS CollegeCode, Colleges.Name AS CollegeName, Courses.College AS CourseCollege, Courses.Code AS CourseCode
                    FROM Colleges LEFT JOIN Courses ON Colleges.Code = Courses.College
                ) AS CollegeQuery
                ON Students.Course = CollegeQuery.CourseCode
                WHERE Students.StudentId LIKE '%{query}%' 
                OR Students.Firstname LIKE '%{query}%' 
                OR Students.Lastname LIKE '%{query}%'
                OR Students.Course LIKE '%{query}%' 
                OR Students.Year LIKE '%{query}%' 
                OR Students.Gender LIKE '%{query}%'
                OR CollegeQuery.CollegeName LIKE '%{query}%' 
                OR CollegeQuery.CollegeCode LIKE '%{query}%';
                """)
                results = list(cursor.fetchall())
                connection.commit()
                return {'success': True, 'results': results}
        except MySQLError as e:
            return {'success': False, 'results': str(e)}
        finally:
            cursor.close()
            connection.close()

    #Count
    @staticmethod
    def count_rows(query=""):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            if query != "":
                cursor.execute(f"""
                SELECT COUNT(*) FROM Students
                WHERE StudentId LIKE '%{query}%' 
                OR Firstname LIKE '%{query}%' 
                OR Lastname LIKE '%{query}%'
                OR Course LIKE '%{query}%' 
                OR Year LIKE '%{query}%' 
                OR Gender LIKE '%{query}%';
                """)
                results = cursor.fetchone()[0]
                connection.commit()
                return {'success': True, 'results': int(results)}
            else:
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

    #Upload Image
    @staticmethod
    def upload_image_url(student_id, url=""):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            UPDATE Students SET ImgURL = '{}' WHERE StudentId = '{}';
            """.format(url, student_id)
            )
            connection.commit()
            return {'success': True, 'results': "Uploaded the image url {} of {} into Students table successfuly".format(url, student_id)}
        except MySQLError as e:
            return {'success':False, 'results':str(e)}
        finally:
            cursor.close()
            connection.close()
    
    # # GetName
    # @staticmethod
    # def get_name(student_id):
    #     connection = DatabaseService().connect()
    #     cursor = connection.cursor()
    #     try:
    #         cursor.execute("""
    #         SELECT Firstname, Lastname FROM Students WHERE StudentId = '{}';
    #         """).format(str(student_id))
    #         result = ""
    #         data = cursor.fetchone()[0]
    #         if data == "":
    #             result = data
    #         connection.commit()
    #         return {'success': True, 'results': result}
    #     except MySQLError as e:
    #         return {'success': False, 'results': str(e)}
    #     finally:
    #         cursor.close()
    #         connection.close()

    @staticmethod
    def create_table(connection):
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students(
            StudentId char(9) NOT NULL,
            Firstname char(150) NOT NULL,
            Lastname char(150) NOT NULL, 
            Course char(20),
            Year enum('1st','2nd','3rd','4th') NOT NULL,
            Gender enum('Woman','Man','Transgender','Non-binary/Non-conforming','Prefer not to respond') NOT NULL,             
            ImgURL varchar(1000) NOT NULL,
            PRIMARY KEY (StudentId),
            FOREIGN KEY (Course) REFERENCES Courses(Code) ON UPDATE CASCADE ON DELETE SET NULL
        ) ENGINE=INNODB;
        """)