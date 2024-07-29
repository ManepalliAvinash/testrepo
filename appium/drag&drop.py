import time

from appium import webdriver
from typing import Any,Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

cap:Dict[str,Any]={
  "platformName": "Android",
  "appium:deviceName": "Android",
  "appPackage":"com.mobeta.android.demodslv",
  "appActivity":"com.mobeta.android.demodslv.TestBedDSLV"
}

url='http://localhost:4723/wd/hub'

driver=webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))
driver.find_element(by=AppiumBy.ID,value="com.mobeta.android.demodslv:id/activity_desc").click()
elm=driver.find_elements(by=AppiumBy.ID,value="com.mobeta.android.demodslv:id/text")
action=TouchAction(driver)
action.press(elm[0]).wait(3000).move_to(elm[4]).perform().release()
time.sleep(10)
driver.quit()