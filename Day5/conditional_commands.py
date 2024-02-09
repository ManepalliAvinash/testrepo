from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()

#is_displayed
#search_box=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
#print("dispaly_status : ",search_box.is_displayed())

#is_enabled
print("display_status : ",search_box.is_enabled())
driver.close()

#is_selected
"""rd_male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
rd_female=driver.find_element(By.XPATH,"//input[@id='gender-female']")
print("before_status : ",rd_male.is_selected())
print("before_status : ",rd_female.is_selected())

rd_male.click()
rd_female.click()
print("after_status : ",rd_male.is_selected())
print("after_status : ",rd_female.is_selected())
driver.close()"""