# Test case:
"""
1.open web browser(chrome)
2.open url:- " https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
3.enter username: Admin
4.enter browser: admin123
5.click on login
6.capture title of homepage(Actual title)
7.verify title of the page:orangeHRM(Expected)
8.close browser
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.CLASS_NAME,"oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()
actual_title=driver.title
expected_title="OrangeHRM"
if actual_title==expected_title:
    print("login_test_passed")
else:
    print("login_test_failed")
driver.close()

driver.find_elements()