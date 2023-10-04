from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
#1 count number of rows
number_of_rows=driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr")
#print(len(number_of_rows))
#2 count number of columns
number_of_columns=driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr[1]/th")
#print(len(number_of_columns))

#3 reday specfic row and column value
value_of_specfic=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[5]/td[1]")
#print(value_of_specfic.text)

#4 read all the rows and all columns
"""for r in range(2,len(number_of_rows)+1):
    for c in range(1,len(number_of_columns)+1):
        data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]")
        print(data.text,end=" ")
    print()"""

#5 read data based on condiction
for r in range(2,len(number_of_rows)+1):
    Author_Name=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
    if Author_Name=="Mukesh":
        book_name=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[1]").text
        price=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[4]").text
        print(book_name,"    ",Author_Name,"    ",price)
driver.close()

