from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()
"""drpcountry_elm=driver.find_element(By.NAME,"")
drp_country= Select(drpcountry_elm)
drp_country.select_by_visible_text("India")"""

#select option for the dropdown
#drp_country.select_by_visible_text("India")
#drp_country.select_by_value("china")
#drp_country.select_by_index(8)
# capture all the options
"""all_options=drp_country.options
print("length of all options: ",len(all_options))
for option in all_options:
    print(option.text)

#select option fro dropdown without using built in method
for options in all_options:
    if options.text=='India':
        options.click()
        break"""

ctry_ele=driver.find_element_by_name("DateOfBirthDay")
ctry_elm=Select(ctry_ele)
ctry_elm.select_by_visible_text("20")