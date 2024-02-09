from selenium import webdriver


driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# capture cookies from the browser
cookies=driver.get_cookies()
print("size of cookies before:",len(cookies))

# print all details for all cookies
"""for cookie in cookies:
    print(cookie)"""
"""for cookie in cookies:
    print(cookie.get("name"),":",cookie.get("value"))"""

# Add a new cookie to browser

driver.add_cookie({"name":"Mycookie","value":"12345"})
cookies=driver.get_cookies()
print("size of cookies after adding:",len(cookies))

# Delete a specfic cookie

"""driver.delete_cookie("Mycookie")
cookies=driver.get_cookies()
print("size of cookies after delete one cookie:",len(cookies))"""

# Delete all the cookies
"""driver.delete_all_cookies()
cookies=driver.get_cookies()
print("size of cookies after delete all the cookies:",len(cookies))

driver.quit()"""
