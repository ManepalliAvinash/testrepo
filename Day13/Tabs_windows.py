import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
"""driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
Reg_Link=Keys.CONTROL+Keys.RETURN
driver.find_element(By.LINK_TEXT,"Register").send_keys(Reg_Link)"""

# New Tab -Selenium4 :Opens a new tab and switch to new tab

"""First_tab=driver.get("https://www.opencart.com/")
driver.switch_to.new_window('Tab')
second_tab=driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
"""
# New Window -Selenium4 :Opens a new tab and switch to new window   #key word is different for tab and window remaning is same

First_tab=driver.get("https://www.opencart.com/")
driver.switch_to.new_window('window')
second_tab=driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
