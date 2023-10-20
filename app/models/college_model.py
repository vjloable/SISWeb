from flask import g

class CollegeModel:
    def __init__(self, code, name):
        self.code = code
        self.name = name

    def insert(self):
        cursor = g.db_con.cursor()
        cursor.execute("""
        INSERT INTO Colleges
        VALUES ({}, {});
        """.format(self.code, self.name)
        )
    
    def list_all(self):
        cursor = g.db_con.cursor()
        response = cursor.execute("""
        SELECT * FROM Colleges;
        """)
        return response

    @staticmethod
    def create_table():
        cursor = g.db_con.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Colleges( 
            Code char(20) NOT NULL,
            Name char(150) NOT NULL,
            PRIMARY KEY (Code)
        );
        """)