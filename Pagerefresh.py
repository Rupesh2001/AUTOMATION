<<<<<<< HEAD
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))



url= "https://ecommerce.sebs.asia"
driver.get(url)
driver.maximize_window()
time.sleep(4)

#find locator

Logo = driver.find_element(By.XPATH,"//img[@alt='Logo']")
Logo.click()
time.sleep(2)
checkrefresh = driver.find_element(By.XPATH,"//button[normalize-space()='Login']")
 
if checkrefresh.is_displayed:
    print("Page is refreshed")
else:
    print("Page not refreshed")
=======
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))



url= "https://ecommerce.sebs.asia"
driver.get(url)
driver.maximize_window()
time.sleep(4)

#find locator

Logo = driver.find_element(By.XPATH,"//img[@alt='Logo']")
Logo.click()
time.sleep(2)
checkrefresh = driver.find_element(By.XPATH,"//button[normalize-space()='Login']")
 
if checkrefresh.is_displayed:
    print("Page is refreshed")
else:
    print("Page not refreshed")
>>>>>>> 8218050 (Selenium Automation)
driver.quit()