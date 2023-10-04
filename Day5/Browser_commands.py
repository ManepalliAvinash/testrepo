from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
time.sleep(5)
driver.close() # it will close on driver focused

driver.quit() # it will close all browser
