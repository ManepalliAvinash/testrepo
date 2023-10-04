from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Index.html")
driver.maximize_window()
#mail_id=input("enter the mail_id for sign_in: ")
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("groot@gmail.com")
driver.find_element(By.XPATH,"//img[@id='enterimg']").click()
driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("Groot")
driver.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("Tree")
driver.find_element(By.XPATH,"//textarea[@class='form-control ng-pristine ng-untouched ng-valid']").send_keys("lankelapalem,Visakhapatnam")
driver.find_element(By.XPATH,"//input[@type='email']").send_keys("groot@gmail.com")
driver.find_element(By.XPATH,"//input[@type='tel']").send_keys("9390773943")
male=driver.find_element(By.XPATH,"//input[@value='Male']")
print(male.is_displayed())
male.click()
check_boxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for check_box in check_boxes:
    check_box.click()

driver.find_element(By.XPATH,"//div[@id='msdd']").click()
languages=driver.find_elements(By.XPATH,"//multi-select//div[2]/ul/li/a")
for language in languages:
    if language.text=="English":
        language.click()
        break

skills=driver.find_element(By.XPATH,"//select[@id='Skills']")
skills_elm=Select(skills)
skills_elm.select_by_value("Python")

# element not intractable in the website
"""driver.find_element(By.XPATH,"//span[@class='select2-selection select2-selection--single']").click()
countries=driver.find_elements(By.XPATH,"//ul[@id='select2-country-results']/li")
print(len(countries))
for country in countries:
    if country.text=="India":
        country.click()
        break"""

years=driver.find_element(By.XPATH,"//select[@id='yearbox']")
years_elm=Select(years)
years_elm.select_by_value("2001")

months=driver.find_element(By.XPATH,"//select[@placeholder='Month']")
months_elm=Select(months)
months_elm.select_by_value("December")

dates=driver.find_element(By.XPATH,"//select[@id='daybox']")
dates_elm=Select(dates)
dates_elm.select_by_value("27")

password="groot2712"
driver.find_element(By.XPATH,"//input[@id='firstpassword']").send_keys(password)
driver.find_element(By.XPATH,"//input[@id='secondpassword']").send_keys(password)