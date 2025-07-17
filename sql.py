import sqlite3

## Connection to SQLite3

connection = sqlite3.connect("student.db")

## Create a cursor object to insert records,create table or to retrieve
cursor = connection.cursor()

## Create table

table_info = """
CREATE table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);
"""

cursor.execute(table_info)

## Insert some records

cursor.execute('''Insert into STUDENT values ('KRISH','Data Science','A',90)''')
cursor.execute('''Insert into STUDENT values ('SUDHANSHU','Data Science','B',100)''')
cursor.execute('''Insert into STUDENT values ('DARIUS','Data Science','A',86)''')
cursor.execute('''Insert into STUDENT values ('VIKASH','Devops','A',50)''')
cursor.execute('''Insert into STUDENT values ('DIPESH','Devops','A',35)''')

## Display all the records
print("The inserted records are")
data = cursor.execute('''SELECT * from student''')

for row in data:
    print(row)

## Close the connection

connection.commit()
connection.close()
