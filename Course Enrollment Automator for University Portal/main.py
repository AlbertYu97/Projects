from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import os
import smtplib
from email.message import EmailMessage
import time

# Email sending function
def send_email(subject, content):
    msg = EmailMessage()
    msg.set_content(content)
    msg['Subject'] = subject
    msg['From'] = os.environ['EMAIL']
    msg['To'] = os.environ['EMAIL']

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(os.environ['EMAIL'], os.environ['EMAIL_PASSWORD'])
    server.send_message(msg)
    server.quit()

# Environment Variables
os.environ['USERNAME'] = 'your_username_here'
os.environ['PASSWORD'] = 'your_password_here'
os.environ['EMAIL'] = 'your_email_here'
os.environ['EMAIL_PASSWORD'] = 'your_email_password_here'

# Initialize WebDriver
path_to_driver_executable = '/path/to/your/chromedriver'
s = Service(path_to_driver_executable)
driver = webdriver.Chrome(service=s)
driver.maximize_window()

# Login Page
login_url = "https://your_login_url_here"
driver.get(login_url)
wait = WebDriverWait(driver, 10)

# Click login button
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Login to ACORN")]')))
login_button.click()

# Enter username and password
username_field = driver.find_element(By.NAME, 'j_username')
password_field = driver.find_element(By.NAME, 'j_password')
username_field.send_keys(os.environ['USERNAME'])
password_field.send_keys(os.environ['PASSWORD'])

# Click the login button
login_button = driver.find_element(By.NAME, '_eventId_proceed')
login_button.click()

# Navigate to "Enrol & Manage"
enrol_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="#/enrol_and_manage"]')))
enrol_button.click()

# Navigate to 'Course'
course_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="#/courses/0"]')))
course_button.click()

# Infinite loop to keep checking for 'Modify' button
while True:
    # Refresh the page
    driver.refresh()
    
    # Check if the 'Modify' button is enabled
    try:
        modify_button = wait.until(EC.element_to_be_clickable((By.ID, 'plan')))
        button_class = modify_button.get_attribute('class')
        
        if 'enrol disabled' not in button_class:
            modify_button.click()
            print("Enrollment successful!")
            send_email("Enrollment Successful", "You have successfully enrolled in the course.")
            break
        else:
            print("The 'Modify' button is not clickable. Waiting for 30 seconds...")
            time.sleep(30)
    except:
        print("Error encountered. Waiting for 30 seconds...")
        time.sleep(30)
