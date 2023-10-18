class StudentModel:
    def __init__(self, id, name):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.year = year
        self.gender = gender

    def create_table(cursor):
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students(
            ID char(9) NOT NULL,
            FirstName char(150) NOT NULL,
            LastName char(150) NOT NULL, 
            Course char(20),
            Year enum('1st','2nd','3rd','4th') NOT NULL,
            Gender enum('Woman','Man','Transgender','Non-binary/Non-conforming','Prefer not to respond') NOT NULL,              
            UNIQUE KEY ID (ID),
            FOREIGN KEY (Course) REFERENCES Courses(Code) ON DELETE CASCADE,
        ) ENGINE=INNODB;
        """)