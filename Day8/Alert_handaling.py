from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
#opens alert window
driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
time.sleep(5)

alert_window=driver.switch_to.alert

print(alert_window.text)
alert_window.send_keys("Selenium")
#alert_window.accept()               # it close the alert window by perform click action on OK button
alert_window.dismiss()              # it close the alert window by perform click action on Cancle Button
