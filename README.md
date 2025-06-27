# WhatsApp Message Sender Tool

A Python automation tool to send WhatsApp messages to a list of phone numbers from an Excel file using **Selenium** and **WhatsApp Web**.

---

## Features

- Sends a custom message to each number without saving it as a contact.
- Useful for bulk messaging when creating temporary groups or contacting users.

---

## Requirements

### 1. ChromeDriver

- Download the ChromeDriver matching your Chrome version:  
  https://chromedriver.chromium.org/downloads
- Extract and copy the path to the `.exe` file.
- Set the path in the script:
  ```python
  CHROMEDRIVER_PATH = "C:\\path\\to\\chromedriver.exe"
  ```

### 2. Excel File

- Must contain a column titled exactly:
  ```
  Phone No
  ```
- Save the Excel file in the same folder as the script.
- If the file name is not `consumer_numbers.xlsx`, update this line:
  ```python
  df = pd.read_excel("your_filename.xlsx")
  ```

### 3. Custom Message

- Edit this line to set your own message:
  ```python
  message = "Hello, this is a test message from Automation Script."
  ```

## How to Run

1. Clone or download this repository.

2. Install dependencies:
   ```bash
   pip install selenium pandas openpyxl
   ```

3. Open terminal in the script folder.

4. Run the script:
   ```bash
   python whatsapp_sender.py
   ```

5. Chrome will open `https://web.whatsapp.com`.

6. Scan the QR code using your phone.

7. After login, return to the terminal and press Enter when prompted.

8. The script will send messages to the numbers in your Excel file.
