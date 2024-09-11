import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='R@jeevoo7',
    database='rajeev')

mycursor = mydb.cursor()
# mycursor.execute('create database rajeev')

# mycursor.execute('create table student(Id int, Name varchar(15), Address varchar(25))')
# mycursor.execute('alter table student add constraint pk_id primary key(id)')

# mycursor.execute('insert into student values(4, "Shubham Kumar", "Bihar")')
# mydb.commit()

# sql1 = 'delete from student where id = 4'
# mycursor.execute(sql1)
# mydb.commit()
sql2 = 'select * from student order by name'
mycursor.execute(sql2)
myresult = mycursor.fetchall()
for i in myresult:
    print(i)
print(mycursor.rowcount, "record(s) ")
# mycursor.execute('')
