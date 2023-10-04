from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://mypage.rediff.com/")
driver.find_element(By.XPATH,"//input[contains(@value,'Go')]").click()
alert_element=driver.switch_to.alert
alert_element.accept()