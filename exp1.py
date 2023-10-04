from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.dummyticket.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[contains(text(),'Buy Ticket')]").click()
driver.find_element(By.XPATH,"//input[@id='product_550']").click()
driver.find_element(By.XPATH,"//input[@id='travname']").send_keys("Groot")
driver.find_element(By.XPATH,"//input[@id='travlastname']").send_keys("Green")
driver.find_element(By.XPATH,"//*[@id='dob']").click()
month_elm=driver.find_element(By.XPATH,"//select[@aria-label='Select month']")
drp_month=Select(month_elm)
drp_month.select_by_visible_text("Dec")


year_elm=driver.find_element(By.XPATH,"//select[@aria-label='Select year']")
drp_year=Select(year_elm)
drp_year.select_by_visible_text("2001")

dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for elm in dates:
    if elm.text=="27":
        elm.click()
        break

driver.find_element(By.XPATH,"//input[@id='sex_1']")
driver.find_element(By.XPATH,"//input[@id='fromcity']").send_keys("Chennai")
driver.find_element(By.XPATH,"//input[@id='tocity']").send_keys("Visakhapatnam")
driver.find_element(By.XPATH,"//input[@id='departon']").click()



driver.find_element(By.XPATH,"//*[@id='departon']").click()
month_elm=driver.find_element(By.XPATH,"//select[@aria-label='Select month']")
drp_month=Select(month_elm)
drp_month.select_by_visible_text("Dec")


year_elm=driver.find_element(By.XPATH,"//select[@aria-label='Select year']")
drp_year=Select(year_elm)
drp_year.select_by_visible_text("2024")

dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for elm in dates:
    if elm.text=="27":
        elm.click()
        break

driver.find_element(By.XPATH,"//*[@id='select2-reasondummy-container']").click()
driver.find_element(By.XPATH,"//input[@role='combobox']").send_keys("Visa Application")
driver.find_element(By.XPATH,"//input[@role='combobox']").submit()