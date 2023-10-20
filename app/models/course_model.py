class CourseModel:
    def __init__(self, code, name):
        self.code = code
        self.name = name

    @staticmethod
    def create_table(cursor):
        cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Courses(
            code char(20) NOT NULL,
            name char(150) NOT NULL,
            college char(20),
            PRIMARY KEY (code),
            FOREIGN KEY (college) REFERENCES Colleges(id) ON DELETE CASCADE
        );
        """)