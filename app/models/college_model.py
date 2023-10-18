class CollegeModel:
    def __init__(self, code, name):
        self.code = code
        self.name = name

    def create_table(cursor):
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Colleges(
            ID char(20) NOT NULL,
            Name char(150) NOT NULL,
            KEY ID (ID)
        ) ENGINE=INNODB;
        """)