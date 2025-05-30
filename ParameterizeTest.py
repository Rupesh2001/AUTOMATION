<<<<<<< HEAD
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Fixture
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://ecommerce.sebs.asia/login")
    driver.maximize_window()
    time.sleep(5)
    yield driver
    driver.quit()

# Parametrize: run test 5 times with same data
@pytest.mark.parametrize("email, password", [
    ("your_email@example.com", "your_password"),
    ("your_emailexample.com", "your_password"),
    ("your_email@examplecom", "your_password"),
    ("youremail@example.com", "your_password"),
    ("your", "your_password"),
])
def test_login_invalid(driver, email, password):
    email_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter email']")
    password_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']")
    email_input.clear()
    password_input.clear()

    email_input.send_keys(email)
    password_input.send_keys(password)

    login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']")
    login_button.click()

    time.sleep(2)  # ideally use WebDriverWait instead

    error_msg_element = driver.find_element(By.XPATH, "//div[@role='status']")
    error_msg = error_msg_element.text.strip()
    assert error_msg == "Invalid username or password. Please try again.", "Unexpected login error message."
    
=======
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Fixture
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://ecommerce.sebs.asia/login")
    driver.maximize_window()
    time.sleep(5)
    yield driver
    driver.quit()

# Parametrize: run test 5 times with same data
@pytest.mark.parametrize("email, password", [
    ("your_email@example.com", "your_password"),
    ("your_emailexample.com", "your_password"),
    ("your_email@examplecom", "your_password"),
    ("youremail@example.com", "your_password"),
    ("your", "your_password"),
])
def test_login_invalid(driver, email, password):
    email_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter email']")
    password_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']")
    email_input.clear()
    password_input.clear()

    email_input.send_keys(email)
    password_input.send_keys(password)

    login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']")
    login_button.click()

    time.sleep(2)  # ideally use WebDriverWait instead

    error_msg_element = driver.find_element(By.XPATH, "//div[@role='status']")
    error_msg = error_msg_element.text.strip()
    assert error_msg == "Invalid username or password. Please try again.", "Unexpected login error message."
    
>>>>>>> 8218050 (Selenium Automation)
