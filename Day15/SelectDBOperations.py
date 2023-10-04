import mysql.connector

con=mysql.connector.connect(host="localhost",port=3306,user="root",password="root",database="groot")
curs=con.cursor()

curs.execute("select * from student_list")
for row in curs:
    print(row[0],row[1],row[2])