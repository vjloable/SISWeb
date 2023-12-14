from app.services.database_service import DatabaseService
from mysql.connector import Error as MySQLError

class CollegeModel:

    #Create
    @staticmethod
    def insert(code, name, img_url=""):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            INSERT INTO Colleges (Code, Name, ImgURL) 
            VALUES ("{}", "{}", "{}");
            """.format(code, name, img_url)
            )
            connection.commit()
            return {'success':True, 'results':"Inserted ({}, {}, {}) into Colleges table successfuly".format(code, name, img_url)}
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
    def update(code, new_code, new_name, img_url):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            UPDATE Colleges SET Code = '{}', Name = '{}', ImgURL = '{}' WHERE Code = '{}';
            """.format(new_code, new_name, code, img_url)
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

    # List
    @staticmethod
    def get_list(offset, query="",):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            if offset >= 0:
                if query == "":
                    cursor.execute(f"""
                    SELECT * FROM Colleges
                    LIMIT 11 
                    OFFSET {offset};
                    """)
                    results = list(cursor.fetchall())
                    connection.commit()
                    return {'success': True, 'results': results}
                else:
                    cursor.execute(f"""
                    SELECT * FROM Colleges
                    WHERE Code LIKE '%{query}%' OR 
                    Name LIKE '%{query}%'
                    LIMIT 11 
                    OFFSET {offset};
                    """)
                    results = list(cursor.fetchall())
                    success = len(results) > 0
                    connection.commit()
                    return {'success': success, 'results': results}
            else:
                cursor.execute(f"""
                SELECT * FROM Colleges
                WHERE Code LIKE '%{query}%' OR 
                Name LIKE '%{query}%';
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
                SELECT COUNT(*) FROM Colleges
                WHERE Code LIKE '%{query}%' OR 
                Name LIKE '%{query}%';
                """)
                results = cursor.fetchone()[0]
                connection.commit()
                return {'success':True, 'results':int(results)}
            else:
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
    
    # Upload Image
    @staticmethod
    def upload_image_url(code, url=""):
        connection = DatabaseService().connect()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            UPDATE Colleges SET ImgURL = '{}' WHERE Code = '{}';
            """.format(url, code)
            )
            connection.commit()
            return {'success': True, 'results': "Uploaded the image url {} of {} into Colleges table successfuly".format(url, code)}
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
    #         SELECT Name FROM Colleges WHERE Code = '{}';
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
        CREATE TABLE IF NOT EXISTS Colleges(
            Code char(20) NOT NULL,
            Name char(150) NOT NULL,
            ImgURL varchar(1000) NOT NULL,
            PRIMARY KEY (Code)
        ) ENGINE=INNODB;
        """)