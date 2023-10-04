#explicit_wait
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()


mywait=WebDriverWait(driver,10,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException,Exception])
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element(By.XPATH, "//textarea[@id='APjFqb']").send_keys("Selenium")
driver.find_element(By.XPATH, "//textarea[@id='APjFqb']").submit()
search_link=mywait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))
search_link.click()
driver.quit( )