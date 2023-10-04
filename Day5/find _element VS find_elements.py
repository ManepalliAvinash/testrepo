from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")

####### find element
#1 Locator matching with single web element
#element=driver.find_element(By.XPATH,"//*[@id='small-searchterms']")
#element.send_keys("Lenovo Thinkpad X1 Carbon Laptop")

#2 Locator matching with multiple web element
#element=driver.find_element(By.XPATH,"//div [@class='footer']//a")
#print(element.text) #sitemap

#3 Element not avaliable then throw NosuchElement Exception

#element=driver.find_element(By.LINK_TEXT,"Login")
#element.click()

# find elements() ---------return multiple webelement

#1 locator matching with single web element
#element=driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
#print(len(element))
#element[0].send_keys("Lenovo Thinkpad X1 Carbon Laptop")

#2 locator matching with multiple web element
#element=driver.find_elements(By.XPATH,"//div [@class='footer']//a")
#print(len(element)) #23
#for i in element:
#    print(i.text)

#3 element not avilable
element=driver.find_elements(By.LINK_TEXT,"Log")
print(len(element))

driver.close()

