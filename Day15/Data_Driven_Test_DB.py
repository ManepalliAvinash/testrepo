import time
import mysql.connector
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(
    "https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.maximize_window()

try:
    con = mysql.connector.connect(host="localhost", port=3306, user="root", password="root", database="automation")
    curs = con.cursor()
    curs.execute("select * from caldata")
    for row in curs:
        princ = row[0]
        roi = row[1]
        Period1 = row[2]
        Period2 = row[3]
        Freq = row[4]
        Expt_Mart_value = row[5]

        # Passing Data to application

        driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(princ)
        driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(roi)
        driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(Period1)
        Time = driver.find_element(By.XPATH, "//select[@id='tenurePeriod']")
        Time_elm = Select(Time)
        Time_elm.select_by_visible_text(Period2)
        Compd_Freq = driver.find_element(By.XPATH, "//*[@id='frequency']")
        Compd_Freq_elm = Select(Compd_Freq)
        Compd_Freq_elm.select_by_visible_text(Freq)
        # clc=driver.find_element(By.CSS_SELECTOR,"img[src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']")
        # clc.click()
        driver.find_element(By.XPATH, '//*[@id="fdMatVal"]/div[2]/a[1]').click()
        Maturity_Value = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong")

        # Validation

        if float(Expt_Mart_value) == float(Maturity_Value.text):
            print("Test passed")
        else:
            print("Test Failed")

        # Clear the data after completing one set of data
        driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img").click()
        time.sleep(5)
except:
    print("coonection unsucessful")

driver.close()
