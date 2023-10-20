class CourseModel:
    def __init__(self, code, name):
        self.code = code
        self.name = name

    @staticmethod
    def create_table(connection):
        cursor = connection.cursor()
        cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Courses(
            Code char(20) NOT NULL,
            Name char(150) NOT NULL,
            College char(20),
            PRIMARY KEY (Code),
            FOREIGN KEY (College) REFERENCES Colleges(Code) ON DELETE CASCADE
        );
        """)