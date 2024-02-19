import time

from appium import webdriver
from typing import Any,Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap:Dict[str,Any]={
  "platformName": "Android",
  "appium:deviceName": "Android",
  #"appPackage":"com.samsung.android.dialer",
  #"appActivity":"com.samsung.android.dialer.DialtactsActivity",
  "appPackage":"com.sec.android.app.popupcalculator",
  "appActivity":"com.sec.android.app.popupcalculator.Calculator"
}

url='http://localhost:4723/wd/hub'

driver=webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))
driver.find_element(by=AppiumBy.XPATH,value="//android.widget.Button[@content-desc='5']").click()
driver.find_element(by=AppiumBy.XPATH,value="//android.widget.Button[@content-desc='Plus']").click()
driver.find_element(by=AppiumBy.ID,value="com.sec.android.app.popupcalculator:id/calc_keypad_btn_05").click()
driver.find_element(by=AppiumBy.XPATH,value="//android.widget.Button[@content-desc='Equal']").click()
actual_value=driver.find_element(by=AppiumBy.XPATH,value="//android.widget.EditText[@resource-id='com.sec.android.app.popupcalculator:id/calc_edt_formula']").text
expected_value="10"
actual_value=actual_value[:2]
print(actual_value)
if expected_value==actual_value:
  print("Test Passed")
else:
  print("Test Failed")

time.sleep(10)
driver.quit()