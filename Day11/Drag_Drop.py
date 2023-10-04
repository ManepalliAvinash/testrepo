from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

"""driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)
driver.maximize_window()
Drag=driver.find_element(By.XPATH,"//*[@id='draggable']")
Drop=driver.find_element(By.XPATH,"//*[@id='droppable']")

act=ActionChains(driver)
act.drag_and_drop(Drag,Drop).perform()"""

driver=webdriver.Chrome()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.implicitly_wait(10)
driver.maximize_window()

Rome=driver.find_element(By.XPATH,"//div[@id='box6']")
Italy=driver.find_element(By.XPATH,"//div[@id='box106']")

madrid=driver.find_element(By.XPATH,"//div[@id='box7']")
spain=driver.find_element(By.XPATH,"//div[@id='box107']")

Oslo=driver.find_element(By.XPATH,"//div[@id='box1']")
Norway=driver.find_element(By.XPATH,"//div[@id='box101']")

Copenhagen=driver.find_element(By.XPATH,"//div[@id='box4']")
Denmark=driver.find_element(By.XPATH,"//div[@id='box104']")

seoul=driver.find_element(By.XPATH,"//div[@id='box5']")
South_korea=driver.find_element(By.XPATH,"//div[@id='box105']")

stockholm=driver.find_element(By.XPATH,"//div[@id='box2']")
sweden=driver.find_element(By.XPATH,"//div[@id='box102']")

washington=driver.find_element(By.XPATH,"//div[@id='box3']")
United_states=driver.find_element(By.XPATH,"//div[@id='box103']")


act=ActionChains(driver)

act.drag_and_drop(Rome,Italy).perform()
act.drag_and_drop(madrid,spain).perform()
act.drag_and_drop(Oslo,Norway).perform()
act.drag_and_drop(Copenhagen,Denmark).perform()
act.drag_and_drop(seoul,South_korea).perform()
act.drag_and_drop(stockholm,sweden).perform()
act.drag_and_drop(washington,United_states).perform()
