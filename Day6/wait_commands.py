# implicit_wait
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element(By.XPATH, "//textarea[@id='APjFqb']").send_keys("Selenium")
driver.find_element(By.XPATH, "//textarea[@id='APjFqb']").submit()
driver.find_element(By.XPATH, "//h3[text()='Selenium']").click()
#time.sleep(5)
driver.quit( )