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
    time.sleep(5)  # Wait for the search box to be ready
    search_box.send_keys("Harry Potter")
    time.sleep(2)  # Wait for the suggestions to appear
    driver.find_element(By.XPATH,"//h6[@class='font-level-2 mb-1 cursor-pointer']").click()
    time.sleep(2)  # Wait for the search results to load
    if driver.current_url == "https://ecommerce.sebs.asia/product/product-detail/HarryPotterYkHWxX3z":
        print("Test passed: Search results page is displayed correctly.")
    else:
        print("Test failed: Search results page is not displayed correctly.")

