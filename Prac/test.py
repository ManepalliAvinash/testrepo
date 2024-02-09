from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()
driver.implicitly_wait(3)
"""driver.find_element(By.XPATH,"//textarea[@id='APjFqb']").send_keys("amazon")
driver.find_element(By.XPATH,"//div[@class='lJ9FBc']//input[@name='btnK']").click()
time.sleep(10)
window_id=driver.current_window_handle
print(window_id)"""
driver.find_element(By.XPATH,"//input[@id='gender-male']").click()
driver.find_element(By.XPATH,"//input[@id='FirstName']").send_keys("Hulk")
driver.find_element(By.XPATH,"//input[@id='LastName']").send_keys("H")
day_eml=driver.find_element(By.XPATH,"//select[@name='DateOfBirthDay']")
day=Select(day_eml)
day.select_by_value("27")
month_eml=driver.find_element(By.XPATH,"//select[@name='DateOfBirthMonth']")
month=Select(month_eml)
month.select_by_visible_text("December")
year_elm=driver.find_element(By.XPATH,"//select[@name='DateOfBirthYear']")
year=Select(year_elm)
year.select_by_value("2001")
driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("hulk123@gmail.com")
driver.find_element(By.XPATH,"//input[@id='Company']").send_keys("Marvel studios")
driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("Hulk2712@")
driver.find_element(By.XPATH,"//input[@id='ConfirmPassword']").send_keys("Hulk2712@")
driver.find_element(By.XPATH,"//button[@id='register-button']").click()
print(driver.title)
time.sleep(5)
driver.quit()