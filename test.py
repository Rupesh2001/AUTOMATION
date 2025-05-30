<<<<<<< HEAD
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
# Fixture
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://ecommerce.sebs.asia/login")
    driver.maximize_window()
    yield driver
    driver.quit()

# Test using the driver fixture
def test_case1(driver):
    # Find locators
    email_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter email']")
    password_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']")
    time.sleep(4)
    # Fill form (replace with actual credentials if needed)
    email_input.send_keys("your_email@example.com")
    password_input.send_keys("your_password")
    time.sleep(4)
    login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']")
    login_button.click()
    time.sleep(3)
    # Optionally, add an assertion or wait here
    error_msg_element = driver.find_element(By.XPATH, "//div[@role='status']")
    error_msg = error_msg_element.text.strip()
    assert error_msg == "Invalid username or password. Please try again.", "Login error message does not match expected."
=======
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
# Fixture
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://ecommerce.sebs.asia/login")
    driver.maximize_window()
    yield driver
    driver.quit()

# Test using the driver fixture
def test_case1(driver):
    # Find locators
    email_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter email']")
    password_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']")
    time.sleep(4)
    # Fill form (replace with actual credentials if needed)
    email_input.send_keys("your_email@example.com")
    password_input.send_keys("your_password")
    time.sleep(4)
    login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']")
    login_button.click()
    time.sleep(3)
    # Optionally, add an assertion or wait here
    error_msg_element = driver.find_element(By.XPATH, "//div[@role='status']")
    error_msg = error_msg_element.text.strip()
    assert error_msg == "Invalid username or password. Please try again.", "Login error message does not match expected."
>>>>>>> 8218050 (Selenium Automation)
