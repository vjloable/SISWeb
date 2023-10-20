class CollegeModel:
    def __init__(self, code, name):
        self.code = code
        self.name = name

    @staticmethod
    def create_table(cursor):
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Colleges( 
            code char(20) NOT NULL,
            name char(150) NOT NULL,
            PRIMARY KEY (code)
        );
        """)