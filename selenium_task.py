from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. Open the browser (Chrome)
driver = webdriver.Chrome()

try:
    # 2. Visit Wikipedia
    print("Opening Wikipedia...")
    driver.get("https://www.wikipedia.org/")

    # 3. Find the search input box (filling a form)
    search_box = driver.find_element(By.ID, "searchInput")
    search_box.send_keys("Python (programming language)")
    
    # 4. Press Enter (performing an action)
    search_box.send_keys(Keys.RETURN)

    # Wait 2 seconds for the page to load
    time.sleep(2)

    # 5. Capture page title and an element text
    print("Page Title is:", driver.title)
    
    heading = driver.find_element(By.ID, "firstHeading")
    print("Main Heading is:", heading.text)

finally:
    # 6. Close the browser
    print("Task finished. Closing browser...")
    time.sleep(3)
    driver.quit()