
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://temp-mail.org/en")
time.sleep(5)
# Use get_attribute to get the value of the input field
temp_mail = driver.find_element(By.XPATH, "//input[@id='mail']").get_attribute("value")
print(f"Your email is: {temp_mail}")
time.sleep(5)
'''
    # Open the target URL in a new tab
driver.execute_script("window.open('https://ecommerce.sebs.asia/user-register', '_blank');")
# Switch to the new tab
driver.switch_to.window(driver.window_handles[-1])
time.sleep(5)
# Now you're on the new tab at the registration page
print("Now on:", driver.current_url)
FirstName = driver.find_element(By.XPATH,"//input[@id='firstName']")
Lastname =  driver.find_element(By.XPATH,"//input[@id='lastName']")
PhoneNumber =  driver.find_element(By.XPATH,"//input[@id='phoneNo']")
Email =  driver.find_element(By.XPATH,"//input[@id='email']")
Password =  driver.find_element(By.XPATH,"//input[@id='password']")
Confirm_Password =  driver.find_element(By.XPATH,"//input[@id='confirmPassword']")
time.sleep(4)
FirstName.send_keys("Ram")
Lastname.send_keys("Karki")
Email.send_keys(temp_mail)
PhoneNumber.send_keys("9861368888")
Password.send_keys("Sebs@123")
Confirm_Password.send_keys("Sebs@123")
driver.execute_script("window.scrollBy(0,100);")
time.sleep(5)
Register = driver.find_element(By.XPATH,"//span[@class='p-3']")
Register.click()
time.sleep(5)
# Switch to (Temp Mail)
driver.switch_to.window(driver.window_handles[-1])
print("Second tab:", driver.current_url)
driver.execute_script("window.scrollBy(0,100);")
time.sleep(20)
driver.find_element(By.XPATH,"//span[@title='noreply@sebs.asia']").click()
time.sleep(20)
otp = driver.find_element(By.XPATH,"//strong[normalize-space()='936670']").text
time.sleep(10)

driver.execute_script("window.open('https://ecommerce.sebs.asia/verify-email', '_blank');")
# Switch to second tab
driver.switch_to.window(driver.window_handles[1])
time.sleep(10)

driver.find_element(By.XPATH,"//input[contains(@placeholder,'Enter 6-digit OTP')]").send_keys(otp)
time.sleep(5)
verifyemail = driver.find_element(By.XPATH,"//button[normalize-space()='Verify Email']")
verifyemail.click()
=======
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://temp-mail.org/en")
time.sleep(5)
# Use get_attribute to get the value of the input field
temp_mail = driver.find_element(By.XPATH, "//input[@id='mail']").get_attribute("value")
print(f"Your email is: {temp_mail}")
time.sleep(5)
'''
    # Open the target URL in a new tab
driver.execute_script("window.open('https://ecommerce.sebs.asia/user-register', '_blank');")
# Switch to the new tab
driver.switch_to.window(driver.window_handles[-1])
time.sleep(5)
# Now you're on the new tab at the registration page
print("Now on:", driver.current_url)
FirstName = driver.find_element(By.XPATH,"//input[@id='firstName']")
Lastname =  driver.find_element(By.XPATH,"//input[@id='lastName']")
PhoneNumber =  driver.find_element(By.XPATH,"//input[@id='phoneNo']")
Email =  driver.find_element(By.XPATH,"//input[@id='email']")
Password =  driver.find_element(By.XPATH,"//input[@id='password']")
Confirm_Password =  driver.find_element(By.XPATH,"//input[@id='confirmPassword']")
time.sleep(4)
FirstName.send_keys("Ram")
Lastname.send_keys("Karki")
Email.send_keys(temp_mail)
PhoneNumber.send_keys("9861368888")
Password.send_keys("Sebs@123")
Confirm_Password.send_keys("Sebs@123")
driver.execute_script("window.scrollBy(0,100);")
time.sleep(5)
Register = driver.find_element(By.XPATH,"//span[@class='p-3']")
Register.click()
time.sleep(5)
# Switch to (Temp Mail)
driver.switch_to.window(driver.window_handles[-1])
print("Second tab:", driver.current_url)
driver.execute_script("window.scrollBy(0,100);")
time.sleep(20)
driver.find_element(By.XPATH,"//span[@title='noreply@sebs.asia']").click()
time.sleep(20)
otp = driver.find_element(By.XPATH,"//strong[normalize-space()='936670']").text
time.sleep(10)

driver.execute_script("window.open('https://ecommerce.sebs.asia/verify-email', '_blank');")
# Switch to second tab
driver.switch_to.window(driver.window_handles[1])
time.sleep(10)

driver.find_element(By.XPATH,"//input[contains(@placeholder,'Enter 6-digit OTP')]").send_keys(otp)
time.sleep(5)
verifyemail = driver.find_element(By.XPATH,"//button[normalize-space()='Verify Email']")
verifyemail.click()

'''