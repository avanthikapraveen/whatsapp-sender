import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROMEDRIVER_PATH = "C:\\Users\\avant\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service)
driver.get("https://web.whatsapp.com")
input("Press Enter after scanning the QR code...")
df = pd.read_excel("consumer_numbers.xlsx")
message = "Hello, this is a test message from Automation Script."
print(f"Total number of messages to be send: {len(df)}")
for index, row in df.iterrows():
    phone_number = str(int(float(row['Phone No']))).strip()
    print(f"Sending message to {phone_number}...")
    try:
        url = f"https://wa.me/{phone_number}"
        driver.get(url)
        time.sleep(5)

        continue_btn = driver.find_element(By.LINK_TEXT, "Continue to Chat")
        continue_btn.click()
        time.sleep(3)

        useweb_button = driver.find_element(By.LINK_TEXT, "use WhatsApp Web")
        useweb_button.click()
        time.sleep(10)

        input_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//footer//div[@contenteditable='true']"))
        )
        input_box.click()
        input_box.send_keys(message)
        input_box.send_keys(Keys.ENTER)
    except Exception as e:
        print(f"Couldn't send the message to {phone_number}:", e)
input("Press Enter to close the browser...")

