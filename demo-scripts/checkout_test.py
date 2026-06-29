"""
checkout_test.py — Selenium test for Acme Corp checkout flow.
This script has BROKEN locators that no longer match the updated UI.
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
    page_url = os.getenv("CHECKOUT_PAGE_URL", "http://localhost:9080/pages/checkout.html")
    driver.get(page_url)
    time.sleep(1)

    # BROKEN: was id="first-name" — now id="first-name-input"
    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("John")

    # BROKEN: was id="last-name" — now id="last-name-input"
    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Doe")

    # BROKEN: was id="address" — now id="shipping-address"
    address = driver.find_element(By.ID, "address")
    address.send_keys("123 Main St, Anytown, USA")

    # BROKEN: was id="card-number" — now id="card-number-input"
    card = driver.find_element(By.ID, "card-number")
    card.send_keys("4242424242424242")

    # BROKEN: was id="expiry" — now id="expiry-date"
    expiry = driver.find_element(By.ID, "expiry")
    expiry.send_keys("12/28")

    # BROKEN: was id="cvv" — now id="security-code"
    cvv = driver.find_element(By.ID, "cvv")
    cvv.send_keys("123")

    # BROKEN: was id="promo-input" — now id="coupon-code"
    promo = driver.find_element(By.ID, "promo-input")
    promo.send_keys("SAVE20")

    # BROKEN: was id="apply-promo" — now id="apply-coupon-btn"
    apply_btn = driver.find_element(By.ID, "apply-promo")
    apply_btn.click()
    time.sleep(0.5)

    # BROKEN: was id="checkout-btn" — now id="place-order-btn"
    checkout_button = driver.find_element(By.ID, "checkout-btn")
    checkout_button.click()

    print("Checkout test passed!")

except Exception as e:
    print(f"Checkout test FAILED: {e}")
    raise

finally:
    driver.quit()
