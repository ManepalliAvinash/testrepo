import time

from appium import webdriver
from typing import Any,Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap:Dict[str,Any]={
  "platformName": "Android",
  "appium:deviceName": "Android",
  "appPackage":"com.samsung.android.dialer",
  "appActivity":"com.samsung.android.dialer.DialtactsActivity",
}

url='http://localhost:4723/wd/hub'

driver=webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(5)
alert=driver.switch_to.alert
alert.accept()
driver.find_element(by=AppiumBy.XPATH,value="//android.widget.TextView[@resource-id='com.samsung.android.dialer:id/tab_text_view' and @text='Contacts']").click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value="Create new contact").click()
time.sleep(5)
#save_list=driver.find_elements(by=AppiumBy.ID,value="com.samsung.android.app.contacts:id/container")
#save_list[6].click()
#time.sleep(5)
driver.find_element(by=AppiumBy.ID,value="com.samsung.android.app.contacts:id/nameEdit").send_keys("Groot5")
driver.find_element(by=AppiumBy.XPATH,value="(//android.widget.RelativeLayout[@resource-id='com.samsung.android.app.contacts:id/titleLayout'])[1]").click()
time.sleep(5)
driver.find_element(by=AppiumBy.XPATH,value="//android.widget.EditText[@text='Phone']").send_keys("7013388005")
driver.find_element(by=AppiumBy.XPATH,value="(//android.widget.LinearLayout[@resource-id='com.samsung.android.app.contacts:id/editor_item_frame'])[3]/android.widget.LinearLayout/android.widget.LinearLayout").click()
time.sleep(5)
driver.find_element(by=AppiumBy.XPATH,value="//android.widget.EditText[@text='Email']").send_keys("groot@gmail.com")
time.sleep(5)
driver.find_element(by=AppiumBy.ID,value="com.samsung.android.app.contacts:id/smallLabel").click()
time.sleep(5)
import os
driver.save_screenshot(os.getcwd()+"\\savecontact.png")
time.sleep(5)
driver.quit()
