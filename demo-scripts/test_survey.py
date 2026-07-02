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

email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
email_input.send_keys("testuser@example.com")
time.sleep(3)

# Click 4-star rating
rating_container = wait.until(EC.presence_of_element_located((By.ID, "rating")))
stars = rating_container.find_elements(By.TAG_NAME, "button")
stars[3].click()
time.sleep(3)

# Select "Good" for product quality
quality_container = wait.until(EC.presence_of_element_located((By.ID, "quality")))
quality_buttons = quality_container.find_elements(By.TAG_NAME, "button")
for btn in quality_buttons:
    if btn.text == "Good":
        btn.click()
        break
time.sleep(3)

# Click Next to go to page 2
next_btn = wait.until(EC.element_to_be_clickable((By.ID, "nextBtn")))
next_btn.click()
time.sleep(3)

# ===== PAGE 2 =====

# Select "Yes" for on time
ontime_container = wait.until(EC.presence_of_element_located((By.ID, "ontime")))
ontime_buttons = ontime_container.find_elements(By.TAG_NAME, "button")
for btn in ontime_buttons:
    if btn.text == "Yes":
        btn.click()
        break
time.sleep(3)

recommend_container = wait.until(EC.presence_of_element_located((By.ID, "recommendation")))
recommend_buttons = recommend_container.find_elements(By.TAG_NAME, "button")
for btn in recommend_buttons:
    if btn.text == "Yes":
        btn.click()
        break
time.sleep(3)

# Fill in the feedback textarea
textarea = wait.until(EC.presence_of_element_located((By.ID, "note")))
textarea.send_keys("Delivery was fast and packaging was great!")
time.sleep(3)

# Submit the form
submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#page2 .submit-btn[type='submit']")))
submit_btn.click()
time.sleep(3)

# Verify success overlay
overlay = wait.until(EC.visibility_of_element_located((By.ID, "successOverlay")))
assert overlay.is_displayed(), "Success overlay not shown"

# Click reset
reset_btn = wait.until(EC.element_to_be_clickable((By.ID, "resetBtn")))
reset_btn.click()

time.sleep(2)
driver.quit()
