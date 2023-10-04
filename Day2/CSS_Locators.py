from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://en-gb.facebook.com/")
driver.maximize_window()

# Tag and ID
#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("groot@gmail.com")
#driver.close()

# Tag and class
#driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("groot@gmail.com")
#driver.close()

# Tag and Attributes
#driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("groot2gmail.com")
#driver.close()

#Tag,class and attributes
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_email]").send_keys("groot@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys("Groot2712@")
print(driver.title)
