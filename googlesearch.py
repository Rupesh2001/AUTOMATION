from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pytest , time

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://ecommerce.sebs.asia/")
    driver.maximize_window()
    time.sleep(2)  # Wait for the page to load completely
    yield driver
    driver.quit()


def test_search_results(driver):
    search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search our global search engine for products']")
    search_box.clear()
    time.sleep(5)  # Wait for the search box to be ready
    search_box.send_keys("Harry Potter")
    time.sleep(5)
    search_box.click()  # Wait for the suggestions to appear
    search_box.send_keys(Keys.ARROW_DOWN)
    time.sleep(5)  # Wait for the suggestions to appear
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)  # Wait for the suggestions to appear
