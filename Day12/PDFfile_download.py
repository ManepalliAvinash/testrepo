import os

from selenium import webdriver
from selenium.webdriver.common.by import By

# will get the cwd
get_cwd=os.getcwd()
def chrome_setup():
    # download file in desired location
    preferences = {"download.default_directory": get_cwd,"plugins.always_open_pdf_externally":True}
    options=webdriver.ChromeOptions()
    options.add_experimental_option("prefs",preferences)
    driver = webdriver.Chrome(options=options)
    return driver


driver = chrome_setup()

driver.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")
driver.maximize_window()
driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()
