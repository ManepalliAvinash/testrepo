import time
from appium import webdriver
from typing import Any,Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap:Dict[str,Any]={
  "platformName": "Android",
  "appium:deviceName": "Android",
  "appPackage":"com.samsung.android.messaging",
  "appActivity":"com.samsung.android.withtalk.ui.composer.ComposerActivity",
}

url='http://localhost:4723/wd/hub'
driver=webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(5)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value="Compose new message").click()
driver.find_element(by=AppiumBy.XPATH,value="//android.widget.EditText[@resource-id='com.samsung.android.messaging:id/recipients_editor_to']").send_keys("7013388705")
driver.find_element(by=AppiumBy.XPATH,value="//android.widget.EditText[@resource-id='com.samsung.android.messaging:id/message_edit_text']").send_keys("Hello Groot!")
driver.find_element(by=AppiumBy.XPATH,value="//android.widget.LinearLayout[@resource-id='com.samsung.android.messaging:id/end_buttons_container']").click()
import os
time.sleep(5)
driver.save_screenshot(os.getcwd()+"\\sendmessage.png")
driver.quit()