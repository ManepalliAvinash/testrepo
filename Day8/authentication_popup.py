from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
# real url
#driver.get("https://the-internet.herokuapp.com/basic_auth")
#syntax : https://username:password@link after https
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")