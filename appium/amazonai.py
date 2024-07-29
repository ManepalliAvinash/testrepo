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
driver.implicitly_wait(5)
el16 = driver.find_element(by=AppiumBy.ID, value="in.amazon.mShop.android.shopping:id/chrome_search_hint_view")
el16.click()
el17 = driver.find_element(by=AppiumBy.ID, value="in.amazon.mShop.android.shopping:id/rs_search_src_text")
el17.send_keys("cricket bat")
el18 = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.Button[@text=\"cricket bat\"])[1]")
el18.click()
el19 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@resource-id=\"search\"]/android.view.View[4]")
el19.click()
el20 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@resource-id=\"add-to-cart-button\"]")
el20.click()
el21 = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.ImageView[@resource-id=\"in.amazon.mShop.android.shopping:id/bottom_tab_button_icon\"])[3]")
el21.click()
el22 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text=\"Proceed to Buy (1 item)\"]")
el22.click()
el23 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text=\"Deliver to this address\"]")
el23.click()
el24 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text=\"Cash on Delivery/Pay on Delivery\"]")
el24.click()
el25 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
el25.click()
el26 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.LinearLayout[@resource-id=\"in.amazon.mShop.android.shopping:id/bottom_overlay_bar_container\"]/android.widget.RelativeLayout")
el26.click()
import os
driver.save_screenshot(os.getcwd()+"\\orderplaced screenshot.png")
driver.quit()"""

"""from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("")
driver.maximize_window()
driver.find_element(By.XPATH,"")
"""