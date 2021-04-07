from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
driver.find_element(By.ID,'Form_submitForm_subdomain').send_keys("abc")