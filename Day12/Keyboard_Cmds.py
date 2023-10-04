"""ctrl+a
ctrl+c
tab
ctrl+v"""

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://text-compare.com/")
driver.maximize_window()
input1=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
input2=driver.find_element(By.XPATH,"//textarea[@id='inputText2']")
input1.send_keys("welcome to selenium")


act=ActionChains(driver)

# input1 ------> Ctrl+A Select all the text
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

#input1 ---------> Ctrl+C copy all the txt in input box 1
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# -----> press Tab key to navigate to input2 box
act.key_down(Keys.TAB).key_up(Keys.TAB)

# input1 is pasted in input2 box -----> Ctrl+v
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

