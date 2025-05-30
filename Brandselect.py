
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ecommerce.sebs.asia")
driver.maximize_window()
time.sleep(3)

# Hover over the "BRAND" menu
brand_menu = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[1]/div/div[1]/div/ul/li[1]"))
)
ActionChains(driver).move_to_element(brand_menu).perform()
time.sleep(2)

vego_click= driver.find_element(By.XPATH,"//div[contains(text(),'Vego Garden')]")
vego_click.click()
time.sleep(2)
open_mac= driver.find_element(By.XPATH,"//body//div[@id='root']//div[contains(@class,'row')]//div[contains(@class,'row')]//div[contains(@class,'row')]//div[1]//div[1]//div[2]")
open_mac.click()
love = driver.find_element(By.XPATH,"//button[@class='btn btn-sm btn-outline-danger rounded-circle']")
love.click()
time.sleep(5)
driver.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ecommerce.sebs.asia")
driver.maximize_window()
time.sleep(3)

# Hover over the "BRAND" menu
brand_menu = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[1]/div/div[1]/div/ul/li[1]"))
)
ActionChains(driver).move_to_element(brand_menu).perform()
time.sleep(2)

vego_click= driver.find_element(By.XPATH,"//div[contains(text(),'Vego Garden')]")
vego_click.click()
time.sleep(2)
open_mac= driver.find_element(By.XPATH,"//body//div[@id='root']//div[contains(@class,'row')]//div[contains(@class,'row')]//div[contains(@class,'row')]//div[1]//div[1]//div[2]")
open_mac.click()
love = driver.find_element(By.XPATH,"//button[@class='btn btn-sm btn-outline-danger rounded-circle']")
love.click()
time.sleep(5)
driver.quit()

