class CollegeModel:
    def __init__(self, code, name):
        self.code = code
        self.name = name

    @classmethod
    def insert(self, cursor):
        cursor.execute("""
        INSERT INTO Colleges
        VALUES ({}, {});
        """.format(self.code, self.name)
        )
    
    @classmethod
    def list_all(self, cursor):
        response = cursor.execute("""
        SELECT * FROM Colleges;
        """)
        return response

    @staticmethod
    def create_table(cursor):
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Colleges( 
            Code char(20) NOT NULL,
            Name char(150) NOT NULL,
            PRIMARY KEY (Code)
        );
        """)