"""import time

from appium import webdriver
from typing import Any,Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap:Dict[str,Any]={
  "platformName": "Android",
  "appium:deviceName": "Android",
}

url='http://localhost:4723/wd/hub'

driver=webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value="WhatsApp").click()"""
"""driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value="Search").click()
driver.refresh()
driver.find_element(by=AppiumBy.ID,value="com.whatsapp:id/search_input").send_keys("Jio")
driver.refresh()"""
"""driver.find_element(by=AppiumBy.XPATH,value="(//android.widget.LinearLayout[@resource-id='com.whatsapp:id/conversations_row_header'])[2]/android.widget.FrameLayout").click()
driver.find_element(by=AppiumBy.ID,value="com.whatsapp:id/entry").send_keys("Hello Groot!")
driver.find_element(by=AppiumBy.ID,value="com.whatsapp:id/send").click()
time.sleep(10)
driver.quit()"""



