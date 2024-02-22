import time
import os
from appium import webdriver
from typing import Any,Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap:Dict[str,Any]={
  "platformName": "Android",
  "appium:deviceName": "Android",
  #"app":"C:\APK's\com-hmh-api-2.apk",
  "appPackage":"com.hmh.api",
  "appActivity":"com.hmh.api.ApiDemos"
}

url='http://localhost:4723/wd/hub'

driver=webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(5)
elm=driver.find_elements(by=AppiumBy.ID,value="android:id/text1")
elm[11].click()
elm_ctrl=driver.find_elements(by=AppiumBy.ID,value="android:id/text1")
elm_ctrl[4].click()
elm_theme=driver.find_elements(by=AppiumBy.ID,value="android:id/text1")
elm_theme[0].click()
driver.find_element(by=AppiumBy.ID,value="com.hmh.api:id/edit").send_keys("Groot")
driver.find_element(by=AppiumBy.ID,value="com.hmh.api:id/check2").click()
driver.find_element(by=AppiumBy.ID,value="com.hmh.api:id/radio2").click()
driver.find_element(by=AppiumBy.ID,value="com.hmh.api:id/toggle1").click()
driver.find_element(by=AppiumBy.ID,value="com.hmh.api:id/toggle2").click()
driver.find_element(by=AppiumBy.ID,value="//android.widget.TextView[@text='textColorPrimary']").click()
drop_lst=driver.find_elements(by=AppiumBy.ID,value="android:id/text1")
drop_lst[2].click()
time.sleep(10)
driver.get_screenshot_as_file(os.getcwd()+"\\controlsData.png")
driver.quit()
