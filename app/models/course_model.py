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
            INSERT INTO Courses (Code, Name, College, ImgURL)
            VALUES ("{}", "{}", "{}", "");
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
            SELECT Courses.Code, Courses.Name, Colleges.Name, Colleges.Code, Courses.ImgURL FROM Courses 
            LEFT JOIN Colleges
            ON Colleges.Code = Courses.College
            WHERE Courses.Code = '{}';
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
    def get_list(offset, query="",):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            if offset >= 0:
                if query == "":
                    cursor.execute(f"""
                    SELECT * FROM Courses
                    LIMIT 11 
                    OFFSET {offset};
                    """)
                    results = list(cursor.fetchall())
                    connection.commit()
                    return {'success': True, 'results': results}
                else:
                    cursor.execute(f"""
                    SELECT * FROM Courses 
                    WHERE Code LIKE '%{query}%' OR 
                    Name LIKE '%{query}%' OR 
                    College LIKE '%{query}%'
                    LIMIT 11 
                    OFFSET {offset}
                    """)
                    results = list(cursor.fetchall())
                    success = len(results) > 0
                    connection.commit()
                    return {'success': success, 'results': results}
            else:
                cursor.execute(f"""
                SELECT * FROM Courses 
                WHERE Code LIKE '%{query}%' OR 
                Name LIKE '%{query}%' OR 
                College LIKE '%{query}%';
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
                SELECT COUNT(*) FROM Courses
                WHERE Code LIKE '%{query}%' OR 
                Name LIKE '%{query}%' OR 
                College LIKE '%{query}%';
                """)
                results = cursor.fetchone()[0]
                connection.commit()
                return {'success': True, 'results': int(results)}
            else:
                cursor.execute("""
                SELECT COUNT(*) FROM Courses;
                """)
                results = cursor.fetchone()[0]
                connection.commit()
                return {'success': True, 'results': int(results)}
        except MySQLError as e:
            return {'success':False, 'results':str(e)}
        finally:
            cursor.close()
            connection.close()

    # Upload Image
    @staticmethod
    def upload_image_url(code, url=""):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            UPDATE Courses SET ImgURL = '{}' WHERE Code = '{}';
            """.format(url, code)
            )
            connection.commit()
            return {'success': True, 'results': "Uploaded the image url {} of {} into Courses table successfuly".format(url, code)}
        except MySQLError as e:
            return {'success': False, 'results': str(e)}
        finally:
            cursor.close()
            connection.close()

    # # GetName
    # @staticmethod
    # def get_name(code):
    #     connection = DatabaseService().connect()
    #     cursor = connection.cursor()
    #     try:
    #         cursor.execute("""
    #         SELECT Name FROM Courses WHERE Code = '{}';
    #         """).format(str(code))
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
        CREATE TABLE IF NOT EXISTS Courses(
            Code char(20) NOT NULL,
            Name char(150) NOT NULL,
            College char(20),
            ImgURL varchar(1000) NOT NULL,
            PRIMARY KEY (Code),
            FOREIGN KEY (College) REFERENCES Colleges(Code) ON UPDATE CASCADE ON DELETE SET NULL
        ) ENGINE=INNODB;
        """)