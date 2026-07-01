from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

driver = webdriver.Chrome()
file_path = os.path.abspath("survey.html")
driver.get("http://localhost:9080/pages/survey.html")
wait = WebDriverWait(driver, 10)

# ===== PAGE 1 =====

email_input = driver.find_element(By.ID, "contact")
email_input.send_keys("testuser@example.com")

# Click 4-star rating
rating_container = driver.find_element(By.ID, "rating")
stars = rating_container.find_elements(By.TAG_NAME, "button")
stars[3].click()

# Select "Good" for product quality
quality_container = driver.find_element(By.ID, "quality")
quality_buttons = quality_container.find_elements(By.TAG_NAME, "button")
for btn in quality_buttons:
    if btn.text == "Good":
        btn.click()
        break

# Click Next to go to page 2
next_btn = driver.find_element(By.ID, "nextBtn")
next_btn.click()

# ===== PAGE 2 =====

# Select "Yes" for on time
ontime_container = driver.find_element(By.ID, "ontime")
ontime_buttons = ontime_container.find_elements(By.TAG_NAME, "button")
for btn in ontime_buttons:
    if btn.text == "Yes":
        btn.click()
        break

recommend_container = driver.find_element(By.ID, "recommend")
recommend_buttons = recommend_container.find_elements(By.TAG_NAME, "button")
for btn in recommend_buttons:
    if btn.text == "Yes":
        btn.click()
        break

# Fill in the feedback textarea
textarea = driver.find_element(By.ID, "note")
textarea.send_keys("Delivery was fast and packaging was great!")

# Submit the form
submit_btn = driver.find_element(By.CSS_SELECTOR, "#page2 .submit-btn[type='submit']")
submit_btn.click()

# Verify success overlay
time.sleep(1)
overlay = driver.find_element(By.ID, "successOverlay")
assert overlay.is_displayed(), "Success overlay not shown"

# Click reset
reset_btn = driver.find_element(By.ID, "resetBtn")
reset_btn.click()

time.sleep(2)
driver.quit()