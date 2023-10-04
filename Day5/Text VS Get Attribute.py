from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/login?returnUrl=%2F")
driver.maximize_window()
element=driver.find_element(By.XPATH,"//input[@id='Email']")
element.clear()
element.send_keys("groot@gmail.com")
print("result of text: ",element.text)
print("result of get attribute(): ",element.get_attribute("value"))

driver.quit() 