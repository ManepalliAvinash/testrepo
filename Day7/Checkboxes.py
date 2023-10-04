import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
enable=driver.find_element(By.XPATH,"//input[@id='male']")
print(enable.is_displayed())
#1 select specfic checkbox
driver.find_element(By.XPATH,"//input[@id='male']").click()

#2 select all the check boxes
check_boxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
# approach 1
#for i in range(len(check_boxes)):
#    check_boxes[i].click()
# approach2
for i in check_boxes:
    i.click()
#driver.quit()

#3 select multiple checkboxes by choice
"""for i in check_boxes:
    week_name=i.get_attribute("id")
    if week_name=="monday" or week_name=="saturday" or week_name=="sunday":
        i.click()"""

#4 select last two checkboxes
"""for i in range(len(check_boxes)-2,len(check_boxes)):
    check_boxes[i].click()"""
#5 select first two checkboxes
"""for i in range(len(check_boxes)):
    if i<2:
        check_boxes[i].click()"""
#6 clear all the selected check boxes:
time.sleep(5)
for i in check_boxes:
    if i.is_selected():
        i.click()