from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/home")
driver.maximize_window()
# click on link
#driver.find_element(By.LINK_TEXT,"Digital downloads").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()

# find no links in page
element=driver.find_elements(By.TAG_NAME,"a")
print("total number of links:",len(element))
for i in element:
    print(i.text)

driver.close()