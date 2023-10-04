from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://snapdeal.com/")
driver.get("https://www.amazon.com/")
driver.back()
driver.forward()
driver.refresh()
driver.quit()