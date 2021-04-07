from datetime import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.find_element(By.NAME,'q').send_keys("naveen automationlabs")
option =driver.find_elements(By.CSS_SELECTOR,'ul.erkvQe li span')
print(len(option))
print(driver.title)

for ele in option:
    print(ele.text)
#driver.quit()
