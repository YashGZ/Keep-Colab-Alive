import os
import time
import random
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# === YOUR SETTINGS ===
COLAB_URL = "https://colab.research.google.com/drive/14-5AoRkSj7OSxL_b9LSNRd-7vXE_3Oj-?usp=sharing"
FIREFOX_PROFILE_PATH = r"C:\Users\ayush\AppData\Roaming\Mozilla\Firefox\Profiles\i7vshcmj.default-release"
GECKODRIVER_PATH = r"C:\Users\ayush\geckodriver.exe"  # Make sure this is correct

# === Set up Firefox options ===
options = Options()
options.set_preference("profile", FIREFOX_PROFILE_PATH)

# === Start Firefox with Geckodriver ===
service = Service(GECKODRIVER_PATH)
driver = webdriver.Firefox(service=service, options=options)

try:
    driver.get(COLAB_URL)
    print("🚀 Opened Colab Notebook.")

    # === Wait for the "Connect" button to appear ===
    connect_button_xpath = '//colab-connect-button'
    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, connect_button_xpath))
    )

    print("✅ Colab Loaded. Keeping it alive...")

    while True:
        try:
            connect_button = driver.find_element(By.XPATH, connect_button_xpath)
            connect_button.click()
            print("🔁 Clicked Connect Button at:", time.strftime("%H:%M:%S"))
        except selenium.common.exceptions.ElementClickInterceptedException:
            print("⚠️ Click failed. Retrying...")

        time.sleep(random.randint(40, 50))  # Wait 40-50 seconds

except Exception as e:
    print("❌ Error:", e)

finally:
    try:
        print("✅ Done. Press Enter to close.")
        input()
        driver.close()
    except Exception:
        print("👋 Exiting...")
