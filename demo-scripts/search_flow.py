"""
search_flow.py — Selenium test for Acme Corp product search.
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
    page_url = os.getenv("SEARCH_PAGE_URL", "http://localhost:9080/pages/search.html")
    driver.get(page_url)
    time.sleep(1)

    # BROKEN: was id="search-input" — now changed to id="product-query"
    search_box = driver.find_element(By.ID, "search-input")
    search_box.clear()
    search_box.send_keys("wireless headphones")

    # BROKEN: was id="search-btn" — now changed to id="find-products-btn"
    search_button = driver.find_element(By.ID, "search-btn")
    search_button.click()
    time.sleep(1)

    # BROKEN: was class="filter-category" — now class="product-category-filter"
    category_filters = driver.find_elements(By.CSS_SELECTOR, ".filter-category")
    assert len(category_filters) > 0
    category_filters[1].click()

    # BROKEN: was class="add-to-cart" — now class="add-to-basket-btn"
    add_buttons = driver.find_elements(By.CSS_SELECTOR, ".add-to-cart")
    assert len(add_buttons) > 0
    add_buttons[0].click()

    # BROKEN: was id="cart-button" — now id="basket-icon"
    cart_icon = driver.find_element(By.ID, "cart-button")
    cart_icon.click()

    print("Search flow test passed!")

except Exception as e:
    print(f"Search flow test FAILED: {e}")
    raise

finally:
    driver.quit()
