"""import mysql.connector
input1="insert into test1 values (1,'Avinash',3)"
input2="insert into test1 values(2,'ganesh',9)"
input3="insert into test1(sno,sname,tests_passed) values(3,'ravi',4)"
input4="insert into test1 values(4,'jenny',6)"
read_data="select * from test1"
connect=mysql.connector.connect(host="localhost",port=3306,user="root",password="root",database="testing")
cursor=connect.cursor()
cursor.execute(input1)
cursor.execute(input2)
cursor.execute(input3)
cursor.execute(input4)
cursor.execute(read_data)
for row in cursor:
    value1=row[0]
    value2=row[1]
    value3=row[2]
    print(value1,value2,value3)
connect.commit()
connect.close()"""
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()
dob_ele=driver.find_elements_by_xpath("//select[@name='DateOfBirthDay']")
dob_elm=Select(dob_ele)
for i in range(len(dob_elm)):
