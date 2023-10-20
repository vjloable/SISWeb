class StudentModel:
    def __init__(self, id, name):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.year = year
        self.gender = gender

    @staticmethod
    def create_table(connection):
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students(
            ID char(9) NOT NULL,
            Firstname char(150) NOT NULL,
            Lastname char(150) NOT NULL, 
            Course char(20),
            Year enum('1st','2nd','3rd','4th') NOT NULL,
            Gender enum('Woman','Man','Transgender','Non-binary/Non-conforming','Prefer not to respond') NOT NULL,              
            PRIMARY KEY (ID),
            FOREIGN KEY (Course) REFERENCES Courses(Code) ON DELETE CASCADE
        );
        """)