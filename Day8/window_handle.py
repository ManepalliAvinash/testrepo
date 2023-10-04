from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[normalize-space()='Open Seperate Multiple Windows']").click()
driver.find_element(By.XPATH,"//button[@onclick='multiwindow()']").click()

#parent_window_ID=driver.current_window_handle
#print(parent_window_ID)

# all windows id
windows_Ids=driver.window_handles
#print(windows_Ids)

parent_windowID=windows_Ids[0]
Child_windowID=windows_Ids[1]
Precedent_windowID=windows_Ids[2]

#switch to parent_window
#driver.switch_to.window(parent_windowID)
#print(driver.title)

# switch to child window
driver.switch_to.window(Child_windowID)
print(driver.title)

