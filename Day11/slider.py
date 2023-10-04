from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
#driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()
driver.implicitly_wait(10)
"""min_slider=driver.find_element(By.XPATH,"//span[1]")
max_slider=driver.find_element(By.XPATH,"//span[2]")

print("location of slider before moving min : ",min_slider.location)
print("location of slider before_moving max : ",max_slider.location)

act=ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,200,0).perform()
act.drag_and_drop_by_offset(max_slider,-29,0).perform()

print("location of min slider :",min_slider.location)
print("location of max slider :",max_slider.location)"""


slider=driver.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
print("before slider location: ",slider.location)

act=ActionChains(driver)
act.drag_and_drop_by_offset(slider,30,0).perform()
print("after slider location :",slider.location)