import time

from appium import webdriver
from typing import Any,Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap:Dict[str,Any]={
  "platformName": "Android",
  "appium:deviceName": "Android",
  "appPackage":"com.samsung.android.dialer",
  "appActivity":"com.samsung.android.dialer.DialtactsActivity"
}

url='http://localhost:4723/wd/hub'

driver=webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))
alert_id=driver.switch_to.alert
alert_id.accept()
time.sleep(5)
driver.find_element(by=AppiumBy.ID,value="com.samsung.android.dialer:id/nine").click()
driver.find_element(by=AppiumBy.ID,value="com.samsung.android.dialer:id/one").click()
driver.find_element(by=AppiumBy.ID,value="com.samsung.android.dialer:id/five").click()
driver.find_element(by=AppiumBy.ID,value="com.samsung.android.dialer:id/four").click()
driver.find_element(by=AppiumBy.ID,value="com.samsung.android.dialer:id/one").click()
driver.find_element(by=AppiumBy.ID,value="com.samsung.android.dialer:id/four").click()
driver.find_element(by=AppiumBy.ID,value="com.samsung.android.dialer:id/zero").click()
driver.find_element(by=AppiumBy.ID,value="com.samsung.android.dialer:id/five").click()
driver.find_element(by=AppiumBy.ID,value="com.samsung.android.dialer:id/eight").click()
driver.find_element(by=AppiumBy.ID,value="com.samsung.android.dialer:id/eight").click()
expected_value="9154140588"
actual_value=driver.find_element(by=AppiumBy.ID,value="com.samsung.android.dialer:id/digits").text
if expected_value==actual_value:
    driver.find_element(by=AppiumBy.ID,value="com.samsung.android.dialer:id/dialButton").click()
    time.sleep(5)
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value="End call").click()
    time.sleep(5)
    driver.quit()
    print("Test Passed")
else:
    driver.find_element(by=AppiumBy.ID,value="com.samsung.android.dialer:id/digits").clear()
    driver.quit()
    print("Test Failed")
print(actual_value)