from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
# Self
#text_msg = driver.find_element(By.XPATH, "//a[contains(text(),'LIC Housing Fi')]/self::a").text
#print(text_msg)

#Parent
#text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'LIC Housing Fi')]/parent::td").text
#print(text_msg)

#Child
#text_msg=driver.find_elements(By.XPATH,"//a[contains(text(),'LIC Housing Fi')]/ancestor::tr/child::td")
#print(len(text_msg))

#ancestor
#text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'LIC Housing Fi')]/ancestor::tr").text
#print(text_msg)

#Decendant
#text_msg=driver.find_elements(By.XPATH,"//a[contains(text(),'LIC Housing Fi')]/ancestor::tr/descendant::*")
#print(len(text_msg))

#following
text_msg=driver.find_elements(By.XPATH,"//a[contains(text(),'LIC Housing Fi')]/ancestor::tr/following::*")
print(len(text_msg))