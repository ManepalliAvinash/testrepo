from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php")
driver.maximize_window()
# ABS xpath
#driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[2]/form[1]/input[4]").send_keys("T-shirts")
#driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[2]/form[1]/button[1]").click()

#Relatice XPATH
#driver.find_element(By.XPATH,"//input[@id='search_query_top']").send_keys("T-shirts")
#driver.find_element(By.XPATH,"//button[@name='submit_search']").click()


# Using OR operator relative xpath
driver.find_element(By.XPATH,"//input[@id='search_query_top' or @name='search_query']").send_keys("T-shirts")
driver.find_element(By.XPATH,"//button[@name='submit_search' and @class='btn btn-default button-search']").click()