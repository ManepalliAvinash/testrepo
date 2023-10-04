from selenium import webdriver
from selenium.webdriver.common.by import By
import os
# will get the cwd
get_cwd=os.getcwd()
def chrome_setup():
    # download file in desired location
    preferences = {"download.default_directory": get_cwd}
    options=webdriver.ChromeOptions()
    options.add_experimental_option("prefs",preferences)
    driver = webdriver.Chrome(options=options)
    return driver


driver = chrome_setup()

driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()
driver.find_element(By.XPATH, "//*[@id='table-files']/tbody/tr[1]/td[5]/a").click()
