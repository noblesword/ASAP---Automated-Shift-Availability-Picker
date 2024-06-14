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
    driver.get('https://auth.campaustralia.com.au/Account/Login?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3De7b09064-3e0d-4244-8ef0-e6205a389429%26redirect_uri%3Dhttps%253A%252F%252Foneteam.campaustralia.com.au%252Fsignin-oidc%26response_mode%3Dform_post%26response_type%3Dcode%2520id_token%26scope%3Dopenid%2520profile%2520roles%2520offline_access%2520ocwteamapi_full_access%2520oneteamapi%2520one_team_app%2520documentmanager_readwrite%26state%3DOpenIdConnect.AuthenticationProperties%253DzuhMwVLVWMt-NR9Be3E08-vlTas5-vAVh02KDVmhaMn_JW0f5FJ9OEERYAtVANh5HUUCZ0BlbX137-9bopX2TJP9CiQOaOcly1e2lDBj2XlnYhCPbqZjIS5gJfjWHoAKEua1Ng6NYmfwbzZ5XIOtwrALdXy4ic3fnEvYDl8brmGXBkaDHuZ5-GzECAaZ9hXa4a60O4QU43fGcT-e0ScKLNbJrmBm5-qT4h2QjmSEH3MCsKNI18i5Ju3m5FpY2FUW%26nonce%3D638539732472325478.MTY5MzVmY2ItOTBiMy00MDJiLWJiMmItYzhjZDRlZjRjZDE5Y2QyYWYyMTUtYmJlMy00MmM3LWFmNjctZjYxMjZlMTgzYTE0%26x-client-SKU%3DID_NET461%26x-client-ver%3D5.6.0.0')  # Replace with the actual login URL
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
