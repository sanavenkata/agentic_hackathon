""" 
login_test.py — Selenium test for Acme Corp login page.
This script has BROKEN locators that no longer match the updated UI.
The self-healing agent should detect and fix these.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time

options = Options()
if os.getenv("SELENIUM_HEADLESS", "true").lower() == "true":
    options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

try:
    page_url = os.getenv("LOGIN_PAGE_URL", "http://localhost:9080/pages/login.html")
    driver.get(page_url)
    time.sleep(1)

    # BROKEN: was id="username" — now changed to id="email-input"
    username_field = driver.find_element(By.ID, "username")
    username_field.clear()
    username_field.send_keys("testuser@acme.com")

    # BROKEN: was id="password" — now changed to id="password-field"
    password_field = driver.find_element(By.ID, "password")
    password_field.clear()
    password_field.send_keys("SecurePass123!")

    # BROKEN: was id="login-btn" — now changed to id="sign-in-button"
    login_button = driver.find_element(By.ID, "login-btn")
    login_button.click()

    # BROKEN: was class="forgot-password" — now changed
    forgot_link = driver.find_element(By.CSS_SELECTOR, ".forgot-password")
    assert forgot_link.is_displayed(), "Forgot password link should be visible"

    print("Login test passed!")

except Exception as e:
    print(f"Login test FAILED: {e}")
    raise

finally:
    driver.quit()
