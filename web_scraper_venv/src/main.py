from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

url = "https://www.yahoo.co.jp/"

driver.get(url)
time.sleep(3)

driver.find_element(By.CLASS_NAME, "_1wsoZ5fswvzAoNYvIJgrU4").send_keys("人工知能")
time.sleep(2)

# driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
# submit_btn.click()
driver.find_element(By.CLASS_NAME, "_1wsoZ5fswvzAoNYvIJgrU4").send_keys(Keys.ENTER)
time.sleep(2)

driver.save_screenshot("yahoo_search.png")

driver.quit()