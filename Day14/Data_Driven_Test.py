import time

from selenium.webdriver.support.select import Select

from Day14 import ExcelUtils
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.maximize_window()
file="C:/Users/SARIKA/Desktop/Excel/Fixed_Deposit.xlsx"
Rows=ExcelUtils.get_rows(file,"Sheet1")

for r in range(2,Rows+1):
    princ=ExcelUtils.read(file,"Sheet1",r,1)
    roi=ExcelUtils.read(file,"Sheet1",r,2)
    Period1=ExcelUtils.read(file,"Sheet1",r,3)
    Period2=ExcelUtils.read(file,"Sheet1",r,4)
    Freq=ExcelUtils.read(file,"Sheet1",r,5)
    Expt_Mart_value=ExcelUtils.read(file,"Sheet1",r,6)

    #Passing Data to application

    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(princ)
    driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(roi)
    driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(Period1)
    Time=driver.find_element(By.XPATH,"//select[@id='tenurePeriod']")
    Time_elm=Select(Time)
    Time_elm.select_by_visible_text(Period2)
    Compd_Freq=driver.find_element(By.XPATH,"//*[@id='frequency']")
    Compd_Freq_elm=Select(Compd_Freq)
    Compd_Freq_elm.select_by_visible_text(Freq)
    #clc=driver.find_element(By.CSS_SELECTOR,"img[src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']")
    #clc.click()
    driver.find_element(By.XPATH,'//*[@id="fdMatVal"]/div[2]/a[1]').click()
    Maturity_Value=driver.find_element(By.XPATH,"//span[@id='resp_matval']/strong")

    #Validation

    if float(Expt_Mart_value)==float(Maturity_Value.text):
        print("Test passed")
        ExcelUtils.write(file,"Sheet1",r,7,"Pass")
        ExcelUtils.fillGreenColor(file,"Sheet1",r,7)
    else:
        print("Test Failed")
        ExcelUtils.write(file,"Sheet1",r,7,"fail")
        ExcelUtils.fillRedColor(file,"Sheet1",r,7)

    # Clear the data after completing one set of data
    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img").click()
    time.sleep(5)

driver.close()





