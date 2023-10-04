from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
# Date of birth
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