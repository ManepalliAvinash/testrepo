from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.automationtesting.in/FileUpload.html")
driver.maximize_window()
file=driver.find_element(By.XPATH,"//input[@id='input-4']").send_keys("C:\Users\SARIKA\Downloads\4353466540.pdf")
