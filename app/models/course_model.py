class CourseModel:
    def __init__(self, code, name):
        self.code = code
        self.name = name

    def create_table(cursor):
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Courses(
            Code char(20) NOT NULL,
            Name char(150) NOT NULL,
            College char(20),
            UNIQUE KEY CODE (CODE),
            FOREIGN KEY (College) REFERENCES Colleges(ID) ON DELETE CASCADE,
        ) ENGINE=INNODB;
        """)