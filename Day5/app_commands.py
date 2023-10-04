from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
title=driver.title
print(title)
url=driver.current_url
print(url)
source=driver.page_source
print(source)

driver.quit()