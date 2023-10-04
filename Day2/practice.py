import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='basicBootstrapForm']/div[1]/div[1]/input").send_keys("Groot")
driver.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("Thor")
driver.find_element(By.CSS_SELECTOR,"textarea[ng-model=Adress]").send_keys("Lankelapalem Visakhapatnam")
driver.find_element(By.XPATH,"//input[@type='email']").send_keys("groot2712@gmail.com")
driver.find_element(By.XPATH,"//input[@type='tel']").send_keys("9390773943")
driver.find_element(By.XPATH,"//label[normalize-space()='Male']").click()
check_boxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for checkbox in check_boxes:
    checkbox.click()

time.sleep(5)
driver.close()
