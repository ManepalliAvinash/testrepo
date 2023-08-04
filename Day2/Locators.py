from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.service import Service
#serv_obj=Service("C:\Drivers\chromedriver-win64\chromedriver")
driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
# Name & id locators
#driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
#driver.find_element(By.NAME,"q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

# Link Text & partial Link text
#driver.find_element(By.LINK_TEXT,"Register").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()
