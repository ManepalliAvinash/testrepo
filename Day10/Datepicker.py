#import time
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)
#driver.find_element(By.ID,"datepicker").send_keys("12/27/2001")
mon="December"
yea="2001"
Date="27"
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()       # opens the datepicker

while True:
    month=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    year=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if mon== month and yea==year:                        # checks the month and year of the input value
        break
    else:
        #driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]/span").click()      # nxt arrow
        driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[1]/span").click()      # previous arrow
# select date

dates=driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']/table/tbody/tr/td/a")
for element in dates:
    if element.text==Date:
        element.click()
        break
time.sleep(5)
driver.close()
