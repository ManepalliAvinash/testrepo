from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php")
driver.maximize_window()
# to find multiple web elements or count the elements
# no of slides in the class name using class name
slider=driver.find_elements(By.CLASS_NAME,"homeslider-container")
print(len(slider))
# number of links
links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))
driver.close()

