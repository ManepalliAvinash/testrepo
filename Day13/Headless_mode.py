"""from selenium import webdriver

def headless_chrome():
    ops=webdriver.ChromeOptions()
    ops.headless=True
    driver=webdriver.Chrome(options=ops)
    return driver


driver=headless_chrome()
driver.get("https://demo.nopcommerce.com/")
title=driver.title
url=driver.current_url
print(title)
print(url)
driver.close()"""



from selenium import webdriver

def chrome_setup():
    ops=webdriver.ChromeOptions()
    ops.headless=True
    driver=webdriver.Chrome(options=ops)
    return driver

driver=chrome_setup()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
print(driver.current_window_handle)
driver.switch_to.new_window("tab")
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")
print(driver.title)
print(driver.current_url)
print(driver.current_window_handle)





























