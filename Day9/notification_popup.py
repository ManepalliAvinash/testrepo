from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://whatmylocation.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"")