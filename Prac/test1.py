import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

"""driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()
url=driver.current_url
print(url)
page_source=driver.page_source
print(page_source)
title=driver.title
print(title)
x=driver.log_types
print(x)
logs=driver.get_log('browser')
print(logs)"""

"""driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
gender=driver.find_element(By.XPATH,"//input[@id='male']")
print(gender.is_displayed())

print(gender.is_enabled())
gender.click()
print(gender.is_selected())
time.sleep(10)
driver.close()"""

"""driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
email=driver.find_element(By.XPATH,"//input[@id='email']")

print(email.text)
email.send_keys("Groot23@gmail.com")
print(email.text)
print(email.get_attribute("value"))

time.sleep(10)
driver.close()"""

"""driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
links=driver.find_elements(By.XPATH,"//div[@class='footer-upper']//a")
for i in links:
    print(i.text)

time.sleep(10)
driver.quit()"""
"""
driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
checkbox=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkbox))
len_box=len(checkbox)"""
"""for box in checkbox:
    day=box.get_attribute('id')
    if day=="sunday" or day=="saturday" or day=="thursday":
        box.click()
time.sleep(10)"""

"""for box in range(len_box-2,len_box):
    checkbox[box].click()
time.sleep(10)"""

"""for box in range(len_box):
    if box<2:
        checkbox[box].click()
time.sleep(10)"""

"""driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
country_elm=driver.find_element(By.XPATH,"//select[@id='country']")
country=Select(country_elm)
#country.select_by_visible_text("India")
#time.sleep(10)
#country.select_by_value("China")
#country.select_by_index(0)
#time.sleep(5)
options=country.options
len_country=len(options)
print(len_country)

#for name in options:
#   print(name.text)
for name in options:
    if name.text=="India":
        name.click()
time.sleep(10)
driver.close()"""
import requests
driver=webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
links=driver.find_elements(By.TAG_NAME,"a")
count=0
for link in links:
    url=link.get_attribute("href")

    try:
        rs=requests.head(url)
    except:
        None
    if rs.status_code>400:
        print("link is broken")
        count+=1
    else:
        print("link is not broken")

print("no of links broken: ",count)
time.sleep(10)
driver.close()