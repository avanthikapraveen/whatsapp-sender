import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

CHROMEDRIVER_PATH = "C:\\Users\\avant\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://web.whatsapp.com")
input("Press Enter after scanning the QR code...")

df = pd.read_excel("consumer_numbers.xlsx")
message = "Hello, this is a test message from Automation Script."
print(f"Total number of messages to be send: {len(df)}")

for index, row in df.iterrows():
    raw_number = str(int(float(row['Phone No'])))
    number = re.sub(r'\D', '', raw_number)
    if len(number) == 10:
        phone_number = number
    else:
        print("Invalid phone number format. Skipping...")
        continue
    print(f"Sending message to {phone_number}...")
    try:
        url = f"https://wa.me/{phone_number}"
        driver.get(url)

        continue_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Continue to Chat"))
        )
        continue_btn.click()

        useweb_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "use WhatsApp Web"))
        )
        useweb_button.click()

        input_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//footer//div[@contenteditable='true']"))
        )
        input_box.click()
        input_box.send_keys(message) 
        input_box.send_keys(Keys.ENTER)
    except Exception as e:
        print(f"Couldn't send the message to {phone_number}:", e)
input("Press Enter to close the browser...")

