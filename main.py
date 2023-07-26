import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open the CSV file
with open('Book1.csv', 'r') as file:
    reader = csv.DictReader(file)

    # Start the web driver
    driver = webdriver.Chrome()
    driver.get('https://kesha.lk?user_id=211')

    for row in reader:
        # Extract the data from the row
        first_name = row['First Name']
        last_name = row['Last Name']
        mobile_number = row['Mobile Number'].replace('94', '0')

        # Find the input fields and submit button
        first_name_field = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.NAME, "firstname"))
        )
        last_name_field = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.NAME, "lastname"))
        )
        mobile_field = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.NAME, "mobile"))
        )
        submit_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn.kesha_btn.w-100.p-2"))
        )

        # Fill in the input fields
        first_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name if last_name else 'RandomLastName')
        mobile_field.send_keys(mobile_number)

        # Submit the form
        submit_button.click()

    # Close the web driver
    driver.quit()

