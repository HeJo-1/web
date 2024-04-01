from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome driver with headless mode (optional)
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# Get a valid URL from the user
a = input("Aratılacak siteyi girin [https://example.com] : ")
while not (a.startswith("http://") or a.startswith("https://")):
    print("Geçersiz URL, lütfen tekrar deneyin.")
    a = input("Aratılacak siteyi girin [https://example.com] : ")

# Open the website
driver.get(a)

# Wait for clickable elements to be visible
clickable_elements = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, "//a[@href] | //button"))
)

# Print the text and the URL of each clickable element
for element in clickable_elements:
    print(f"Text: {element.text},\nURL: {element.get_attribute('href')}")

# Close the driver
driver.quit()