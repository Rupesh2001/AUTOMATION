<<<<<<< HEAD
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url="https://ecommerce.sebs.asia/"
time.sleep(4)
driver.get(url)
time.sleep(4)
driver.maximize_window()
time.sleep(4)

Login_Link=driver.find_element(By.XPATH,"//button[normalize-space()='Login']")
Login_Link.click()
time.sleep(4)

if driver.current_url=="https://ecommerce.sebs.asia/login":
            
            Create_Account = driver.find_element(By.XPATH,"//button[normalize-space()='CREATE ACCOUNT']")
            Create_Account.click()
            time.sleep(4)
            FirstName = driver.find_element(By.XPATH,"//input[@id='firstName']")
            Lastname =  driver.find_element(By.XPATH,"//input[@id='lastName']")
            PhoneNumber =  driver.find_element(By.XPATH,"//input[@id='phoneNo']")
            Email =  driver.find_element(By.XPATH,"//input[@id='email']")
            Password =  driver.find_element(By.XPATH,"//input[@id='password']")
            Confirm_Password =  driver.find_element(By.XPATH,"//input[@id='confirmPassword']")
            time.sleep(4)
            FirstName.send_keys("Ram")
            Lastname.send_keys("Karki")
            Email.send_keys("cobejem152@jazipo.com")
            PhoneNumber.send_keys("9861368888")
            Password.send_keys("Sebs@123")
            Confirm_Password.send_keys("Sebs@123")
            driver.execute_script("window.scrollBy(0,100);")
            time.sleep(5)
            Register = driver.find_element(By.XPATH,"//span[@class='p-3']")
            if Register.is_enabled():
                 time.sleep(4)
                 Register.click()
                 #open in new tab
                 driver.execute_script("window.open('https://temp-mail.org/en', '_blank');")
                 # Switch to the new tab (usually the last one)
                 driver.switch_to.window(driver.window_handles[-1])
                 time.sleep(20)
                 if driver.find_element(By.XPATH,"//input[@id='mail']").text == "cobejem152@jazipo.com":
                   time.sleep(20)
                   email = driver.find_element(By.XPATH,"//span[@title='noreply@sebs.asia']").click()
                   driver.execute_script("window.scrollBy(0,100);")
                   otp = driver.find_element(By.XPATH,"//strong[normalize-space()='936670']").text
                   time.sleep(10)
                   #come back to previous tab
                   driver.get("https://ecommerce.sebs.asia/verify-email")
                   original_tab = driver.current_window_handle
                   driver.switch_to.window(original_tab)
                   print("Returned to:", driver.current_url)
                   time.sleep(10)
                   driver.find_element(By.XPATH,"//input[contains(@placeholder,'Enter 6-digit OTP')]").send_keys(otp)
                   verifyemail = driver.find_element(By.XPATH,"//button[normalize-space()='Verify Email']")
                   verifyemail.click()
                 else:
                     print("Non")
            else:
             print("Button is not available")

else:
 print("Login page not opened")

  
driver.quit()




=======
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url="https://ecommerce.sebs.asia/"
time.sleep(4)
driver.get(url)
time.sleep(4)
driver.maximize_window()
time.sleep(4)

Login_Link=driver.find_element(By.XPATH,"//button[normalize-space()='Login']")
Login_Link.click()
time.sleep(4)

if driver.current_url=="https://ecommerce.sebs.asia/login":
            
            Create_Account = driver.find_element(By.XPATH,"//button[normalize-space()='CREATE ACCOUNT']")
            Create_Account.click()
            time.sleep(4)
            FirstName = driver.find_element(By.XPATH,"//input[@id='firstName']")
            Lastname =  driver.find_element(By.XPATH,"//input[@id='lastName']")
            PhoneNumber =  driver.find_element(By.XPATH,"//input[@id='phoneNo']")
            Email =  driver.find_element(By.XPATH,"//input[@id='email']")
            Password =  driver.find_element(By.XPATH,"//input[@id='password']")
            Confirm_Password =  driver.find_element(By.XPATH,"//input[@id='confirmPassword']")
            time.sleep(4)
            FirstName.send_keys("Ram")
            Lastname.send_keys("Karki")
            Email.send_keys("cobejem152@jazipo.com")
            PhoneNumber.send_keys("9861368888")
            Password.send_keys("Sebs@123")
            Confirm_Password.send_keys("Sebs@123")
            driver.execute_script("window.scrollBy(0,100);")
            time.sleep(5)
            Register = driver.find_element(By.XPATH,"//span[@class='p-3']")
            if Register.is_enabled():
                 time.sleep(4)
                 Register.click()
                 #open in new tab
                 driver.execute_script("window.open('https://temp-mail.org/en', '_blank');")
                 # Switch to the new tab (usually the last one)
                 driver.switch_to.window(driver.window_handles[-1])
                 time.sleep(20)
                 if driver.find_element(By.XPATH,"//input[@id='mail']").text == "cobejem152@jazipo.com":
                   time.sleep(20)
                   email = driver.find_element(By.XPATH,"//span[@title='noreply@sebs.asia']").click()
                   driver.execute_script("window.scrollBy(0,100);")
                   otp = driver.find_element(By.XPATH,"//strong[normalize-space()='936670']").text
                   time.sleep(10)
                   #come back to previous tab
                   driver.get("https://ecommerce.sebs.asia/verify-email")
                   original_tab = driver.current_window_handle
                   driver.switch_to.window(original_tab)
                   print("Returned to:", driver.current_url)
                   time.sleep(10)
                   driver.find_element(By.XPATH,"//input[contains(@placeholder,'Enter 6-digit OTP')]").send_keys(otp)
                   verifyemail = driver.find_element(By.XPATH,"//button[normalize-space()='Verify Email']")
                   verifyemail.click()
                 else:
                     print("Non")
            else:
             print("Button is not available")

else:
 print("Login page not opened")

  
driver.quit()




>>>>>>> 8218050 (Selenium Automation)
