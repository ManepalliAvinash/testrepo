import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()     #//span[@id='select2-billing_country-container']
countries_list=driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
print(len(countries_list))

for country in countries_list:
    if country.text=="Algeria":
        country.click()
        break

time.sleep(10)

driver.close()