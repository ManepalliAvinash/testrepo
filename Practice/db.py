"""import mysql.connector

insert_query1="insert into tab1 values(1,'groot',22)"
insert_query2="insert into tab1 values(2,'hulk',12)"
insert_query3="insert into tab1 values(3,'tody',15)"
insert_query4="insert into tab1 values(4,'honey',null)"
insert_query5="insert into tab1 values(5,'jessy',22)"
update_query="update tab1 set sname='donna' where sno=4"

con=mysql.connector.connect(host="localhost", port=3306, user="root", password="root", database="automation")
curs=con.cursor()

curs.execute(insert_query1)
curs.execute(insert_query2)
curs.execute(insert_query3)
curs.execute(insert_query4)
curs.execute(insert_query5)
curs.execute(update_query)
con.commit()
con.close()"""

import mysql.connector

read_data="select * from caldata"
con=mysql.connector.connect(host="localhost",user="root",password="root",port=3306,database="automation")
curs=con.cursor()
curs.execute(read_data)

for rows in curs:
    print(rows[0])