
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Adjust path to driver if needed
driver = webdriver.Chrome()

# Navigate to your form page
driver.get("http://ecommerce.sebs.asia/create-account")

# Sample test cases
test_cases = [
    {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "phone": "1234567890",
        "password": "Password123!",
        "confirm_password": "Password123!",
        "expect_valid": True
    },
    {
        "first_name": "John123",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "phone": "1234567890",
        "password": "Password123!",
        "confirm_password": "Password123!",
        "expect_valid": False
    },
    {
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe.com",
        "phone": "1234567890",
        "password": "Password123!",
        "confirm_password": "Password123!",
        "expect_valid": False
    },
    {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "phone": "abc123",
        "password": "Password123!",
        "confirm_password": "Password123!",
        "expect_valid": False
    },
    {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "phone": "1234567890",
        "password": "pass",
        "confirm_password": "pass",
        "expect_valid": False
    },
    {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "phone": "1234567890",
        "password": "Password123!",
        "confirm_password": "Password321!",
        "expect_valid": False
    }
]

def fill_form(data):
    driver.find_element(By.NAME, "firstname").clear()
    driver.find_element(By.NAME, "firstname").send_keys(data["first_name"])

    driver.find_element(By.NAME, "lastname").clear()
    driver.find_element(By.NAME, "lastname").send_keys(data["last_name"])

    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "email").send_keys(data["email"])

    driver.find_element(By.NAME, "phone").clear()
    driver.find_element(By.NAME, "phone").send_keys(data["phone"])

    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys(data["password"])

    driver.find_element(By.NAME, "confirm_password").clear()
    driver.find_element(By.NAME, "confirm_password").send_keys(data["confirm_password"])

    driver.find_element(By.ID, "submit").click()

    time.sleep(1)  # Wait for response

for idx, case in enumerate(test_cases):
    print(f"\nRunning Test Case {idx + 1}")
    driver.refresh()
    time.sleep(1)

    fill_form(case)

    # Replace with actual error detection logic — e.g., look for validation messages
    try:
        error = driver.find_element(By.CLASS_NAME, "error")  # Customize selector
        has_error = error.is_displayed()
    except:
        has_error = False

    result = "PASS" if has_error != case["expect_valid"] else "FAIL"
    print(f"Expected Valid: {case['expect_valid']}, Found Error: {has_error} → {result}")

driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Adjust path to driver if needed
driver = webdriver.Chrome()

# Navigate to your form page
driver.get("http://ecommerce.sebs.asia/create-account")

# Sample test cases
test_cases = [
    {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "phone": "1234567890",
        "password": "Password123!",
        "confirm_password": "Password123!",
        "expect_valid": True
    },
    {
        "first_name": "John123",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "phone": "1234567890",
        "password": "Password123!",
        "confirm_password": "Password123!",
        "expect_valid": False
    },
    {
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe.com",
        "phone": "1234567890",
        "password": "Password123!",
        "confirm_password": "Password123!",
        "expect_valid": False
    },
    {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "phone": "abc123",
        "password": "Password123!",
        "confirm_password": "Password123!",
        "expect_valid": False
    },
    {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "phone": "1234567890",
        "password": "pass",
        "confirm_password": "pass",
        "expect_valid": False
    },
    {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "phone": "1234567890",
        "password": "Password123!",
        "confirm_password": "Password321!",
        "expect_valid": False
    }
]

def fill_form(data):
    driver.find_element(By.NAME, "firstname").clear()
    driver.find_element(By.NAME, "firstname").send_keys(data["first_name"])

    driver.find_element(By.NAME, "lastname").clear()
    driver.find_element(By.NAME, "lastname").send_keys(data["last_name"])

    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "email").send_keys(data["email"])

    driver.find_element(By.NAME, "phone").clear()
    driver.find_element(By.NAME, "phone").send_keys(data["phone"])

    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys(data["password"])

    driver.find_element(By.NAME, "confirm_password").clear()
    driver.find_element(By.NAME, "confirm_password").send_keys(data["confirm_password"])

    driver.find_element(By.ID, "submit").click()

    time.sleep(1)  # Wait for response

for idx, case in enumerate(test_cases):
    print(f"\nRunning Test Case {idx + 1}")
    driver.refresh()
    time.sleep(1)

    fill_form(case)

    # Replace with actual error detection logic — e.g., look for validation messages
    try:
        error = driver.find_element(By.CLASS_NAME, "error")  # Customize selector
        has_error = error.is_displayed()
    except:
        has_error = False

    result = "PASS" if has_error != case["expect_valid"] else "FAIL"
    print(f"Expected Valid: {case['expect_valid']}, Found Error: {has_error} → {result}")

driver.quit()

