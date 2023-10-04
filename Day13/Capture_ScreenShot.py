from selenium import webdriver
import os
get_cwd=os.getcwd()
driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
#driver.save_screenshot(get_cwd+"\\homepage.png")

#driver.get_screenshot_as_file(get_cwd+"\\homepage2.png")
driver.close()

