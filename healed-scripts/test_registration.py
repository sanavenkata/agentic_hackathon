"""
Selenium test script for the Registration Form.
All locators have been healed automatically by MCP.
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os


def get_driver():
    """Initialize Chrome WebDriver."""
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver


def test_registration_form():
    """Test the registration form with valid data."""
    driver = get_driver()
    try:
        driver.get("http://localhost:9080/pages/registration.html")
        time.sleep(1)

        print("=== Starting Registration Form Test ===\n")

        print("[Step 1] Filling First Name...")
        driver.find_element(By.ID, "firstName").send_keys("John")

        print("[Step 2] Filling Last Name...")
        driver.find_element(By.ID, "lastName").send_keys("Doe")

        print("[Step 3] Filling Phone Number...")
        driver.find_element(By.ID, "phone").send_keys("+1234567890")

        print("[Step 4] Filling Email...")
        driver.find_element(By.ID, "email").send_keys("john.doe@example.com")

        print("[Step 5] Clicking Submit Button...")
        driver.find_element(By.CLASS_NAME, "btn").click()

        time.sleep(1)
        toast = driver.find_element(By.ID, "toast")
        assert "Registration successful" in toast.text
        print("=== ALL TESTS PASSED ===")
    finally:
        driver.quit()


def test_form_validation():
    """Test form validation with empty fields."""
    driver = get_driver()
    try:
        driver.get("http://localhost:9080/pages/registration.html")
        driver.find_element(By.CLASS_NAME, "btn").click()
        time.sleep(0.5)

        first_field = driver.find_element(By.ID, "f-first")
        assert "invalid" in first_field.get_attribute("class")
        print("=== VALIDATION TEST PASSED ===")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_registration_form()
    test_form_validation()
