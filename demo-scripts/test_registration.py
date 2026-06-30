""" 
Selenium test script for the Registration Form.
Some element locators are intentionally WRONG to demonstrate MCP auto-fix capability.
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
    # options.add_argument("--headless")  # Uncomment for headless mode
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver


def test_registration_form():
    """Test the registration form with valid data."""
    driver = get_driver()

    try:
        # Open the registration form
        form_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
        driver.get(f"file:///{form_path}")
        time.sleep(1)

        print("=== Starting Registration Form Test ===\n")

        # --- Step 1: Fill First Name ---
        print("[Step 1] Filling First Name...")
        first_name_input = driver.find_element(By.ID, "firstName")
        first_name_input.clear()
        first_name_input.send_keys("John")
        print("[Step 1] First Name filled successfully.\n")

        # --- Step 2: Fill Last Name ---
        print("[Step 2] Filling Last Name...")
        last_name_input = driver.find_element(By.ID, "lastName")
        last_name_input.clear()
        last_name_input.send_keys("Doe")
        print("[Step 2] Last Name filled successfully.\n")

        # --- Step 3: Fill Phone Number ---
        print("[Step 3] Filling Phone Number...")
        phone_input = driver.find_element(By.ID, "phone")
        phone_input.clear()
        phone_input.send_keys("+1234567890")
        print("[Step 3] Phone Number filled successfully.\n")

        # --- Step 4: Fill Email Address ---
        print("[Step 4] Filling Email Address...")
        email_input = driver.find_element(By.ID, "email")
        email_input.clear()
        email_input.send_keys("john.doe@example.com")
        print("[Step 4] Email filled successfully.\n")

        # --- Step 5: Click Submit Button ---
        print("[Step 5] Clicking Submit Button...")
        submit_btn = driver.find_element(By.CLASS_NAME, "btn")
        submit_btn.click()
        print("[Step 5] Submit button clicked successfully.\n")

        # --- Step 6: Verify Success Toast ---
        print("[Step 6] Verifying success message...")
        time.sleep(1)
        toast = driver.find_element(By.ID, "toast")
        assert "Registration successful!" in toast.text, "Toast not visible!"
        print("[Step 6] Registration successful! Toast message displayed.\n")

        print("=== ALL TESTS PASSED ===")

    except Exception as e:
        print(f"\n[ERROR] Test failed: {e}")
        raise

    finally:
        time.sleep(2)
        driver.quit()


def test_form_validation():
    """Test form validation with empty fields."""
    driver = get_driver()

    try:
        form_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
        driver.get(f"file:///{form_path}")
        time.sleep(1)

        print("\n=== Starting Validation Test ===\n")

        # --- Click submit without filling anything ---
        print("[Step 1] Clicking submit with empty fields...")
        submit_btn = driver.find_element(By.CLASS_NAME, "btn")
        submit_btn.click()
        time.sleep(0.5)

        # --- Verify error states ---
        print("[Step 2] Checking validation errors...")
        first_field = driver.find_element(By.ID, "f-first")
        assert "invalid" in first_field.get_attribute("class"), "First name field should show error"
        print("[Step 2] Validation errors displayed correctly.\n")

        print("=== VALIDATION TEST PASSED ===")

    except Exception as e:
        print(f"\n[ERROR] Validation test failed: {e}")
        raise

    finally:
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    print("Running Registration Form Tests...\n")
    test_registration_form()
    test_form_validation()
