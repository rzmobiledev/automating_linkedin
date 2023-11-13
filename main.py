import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from dotenv import load_dotenv

load_dotenv()

# open browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.linkedin.com/home")

# step login to linkedin
email = driver.find_element(by=By.NAME, value="session_key")
password = driver.find_element(by=By.NAME, value="session_password")
button = driver.find_element(by=By.CSS_SELECTOR, value="button.btn-primary")

email.send_keys(os.environ.get("MY_USERNAME"))
password.send_keys(os.environ.get("PASSWORD"))
button.click()

time.sleep(2)
# search for jobs
search_input = driver.find_element(by=By.CSS_SELECTOR, value="input.search-global-typeahead__input")
search_input.send_keys("Python")
search_input.send_keys(Keys.ENTER)

time.sleep(5)
# click jobs tag
job_tags = driver.find_elements(by=By.CSS_SELECTOR, value="ul.reusable-search__entity-cluster--quick-filter-action-container")
remote = job_tags[0].find_element(by=By.CSS_SELECTOR, value="a")
remote.click()

time.sleep(5)
easy_apply = driver.find_element(by=By.CSS_SELECTOR, value="div.jobs-apply-button--top-card button")
easy_apply.click()