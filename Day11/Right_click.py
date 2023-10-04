import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
driver.implicitly_wait(10)
right_elm=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")

act=ActionChains(driver)
act.context_click(right_elm).perform()      # right click
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/ul/li[3]/span").click()
time.sleep(3)
driver.switch_to.alert.accept()