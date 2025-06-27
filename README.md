# WhatsApp Message Sender Tool

A Python automation tool to send WhatsApp messages to a list of phone numbers from an Excel file using **Selenium** and **WhatsApp Web**.

---

## Features

- Sends a custom message to each number without saving it as a contact.
- Useful for bulk messaging when creating temporary groups or contacting users.
- Automatically handles common formatting issues in phone numbers (e.g., `.0`, spaces, dashes).

---

## Requirements

### 1. ChromeDriver

- Download the correct version of **ChromeDriver** from:  
  https://chromedriver.chromium.org/downloads
- It must match your version of Chrome.
- After downloading, extract it and note the path to the `.exe` file.
- Update this line in the Python script with the correct path:
  CHROMEDRIVER_PATH = "C:\\path\\to\\chromedriver.exe"

### 2. Excel File

- The Excel file should have a column titled exactly:
  Phone No
- Save the Excel file in the same folder as the Python script.
- If your Excel file is not named consumer_numbers.xlsx, update this line:
  df = pd.read_excel("your_filename.xlsx")

### 3. Custom Message

Change this line in the script to send your own message:
message = "Hello, this is a test message from Automation Script."

---

## How to Run

1. Ensure Python and all dependencies (selenium, pandas, openpyxl) are installed.
   pip install selenium pandas openpyxl
2. Open your terminal in the project folder.
3. Run the script:
   python whatsapp_sender.py
4. A Chrome window will open. It will load https://web.whatsapp.com.
5. Scan the QR code using your WhatsApp mobile app.
6. Once you're logged in, go back to the terminal and press Enter as prompted.
7. The script will now send your message to all the phone numbers listed in the Excel file.
