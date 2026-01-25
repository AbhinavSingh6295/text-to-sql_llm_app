import sqlite3

## connect to sqllite
connection = sqlite3.connect('student.db')

## Create a cursor object to insert record, create table, retrieve record, update record, delete record
cursor = connection.cursor()

## Create table
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME VARCHAR(20),
    CLASS VARCHAR(20),
    SECTION VARCHAR(20),
    MARKS INT
    );
"""

cursor.execute(table_info)

## Insert some records

cursor.execute(""" INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('John', 'Data Science', 'A', 90); """)
cursor.execute(""" INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Jane', 'Data Science', 'B', 85); """)
cursor.execute(""" INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Jim', 'Data Science', 'C', 80); """)
cursor.execute(""" INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Jill', 'DevOps', 'D', 75); """)
cursor.execute(""" INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Jack', 'Data Science', 'E', 70); """)
cursor.execute(""" INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Jill', 'DevOps', 'F', 65); """)
cursor.execute(""" INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Jack', 'Data Science', 'G', 60); """)
cursor.execute(""" INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Jill', 'Data Science', 'H', 55); """)
cursor.execute(""" INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Jack', 'Data Science', 'I', 50); """)
cursor.execute(""" INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Jill', 'Data Science', 'J', 45); """)
cursor.execute(""" INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Jack', 'Data Science', 'K', 40); """)

print("The inserted records are:")
data = cursor.execute("SELECT * FROM STUDENT")

for row in data:
    print(row)

# Close the connection
connection.commit()
connection.close()