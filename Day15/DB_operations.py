# insert,updtae,delete,select
import mysql.connector

insert_query="insert into tab1 values(1,'hulk',30)"
insert_query2="insert into tab1 values(2,'ant man',22)"
insert_query3="insert into tab1 values(3,'groot',NULL)"
delete_query="delete from tab1 where sno=2"
update_query="update tab1 set sname='thor' where sname='groot'"

con=mysql.connector.connect(host="localhost",port=3306,user="root",password="root",database="automation")
curs=con.cursor()
curs.execute(insert_query)
curs.execute(insert_query2)
curs.execute(insert_query3)
curs.execute(update_query)
curs.execute(delete_query)
con.commit()
con.close()

print("finished")