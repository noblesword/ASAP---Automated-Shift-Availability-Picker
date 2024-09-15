import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Selenium WebDriver (using Chrome in this example)
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Function to log in
def login(username, password):
    driver.get('https')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username'))).send_keys(username)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password'))).send_keys(password)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'login_button'))).click()
    # Handle pop-up if needed
    time.sleep(2)  # Adjust this based on the actual load time
    driver.switch_to.alert.accept()

# Function to check shifts table and print details of cells with specific color
def check_shifts():
    driver.get('https://oneteam.campaustralia.com.au/shifts')  # Replace with the actual shifts URL
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'portlet-body')))
    shifts_table = driver.find_element(By.CLASS_NAME, 'portlet-body')
    cells = shifts_table.find_elements(By.TAG_NAME, 'td')
    for cell in cells:
        color = cell.value_of_css_property('background-color')
        if color == 'rgb(92,229,186)':  # The RGB equivalent of 
            print(cell.text)

# Main function
def main():
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')

    login(username, password)
    check_shifts()

if __name__ == "__main__":
    main()

# Close the browser after the script is done
driver.quit()
