class StudentModel:
    def __init__(self, id, name):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.year = year
        self.gender = gender

    @staticmethod
    def create_table(cursor):
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students(
            id char(9) NOT NULL,
            firstname char(150) NOT NULL,
            lastname char(150) NOT NULL, 
            course char(20),
            year enum('1st','2nd','3rd','4th') NOT NULL,
            gender enum('Woman','Man','Transgender','Non-binary/Non-conforming','Prefer not to respond') NOT NULL,              
            PRIMARY KEY (id),
            FOREIGN KEY (course) REFERENCES Courses(code) ON DELETE CASCADE
        );
        """)