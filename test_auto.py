import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,800")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(5)
    return driver


def open_page(driver, URL):
    driver.get(URL)


def get_element_by_id(driver, locator):
    return driver.find_element(By.ID, locator)


def element_click(driver, locator):
    element = get_element_by_id(driver, locator)
    element.click()


def element_send_keys(driver, locator, text):
    element = get_element_by_id(driver, locator)
    element.send_keys(text)


def login(driver, username, password):
    element_send_keys(driver, "user-name", username)
    element_send_keys(driver, "password", password)
    element_click(driver, "login-button")


driver = get_driver()
open_page(driver, URL)
login(driver, USERNAME, PASSWORD)
time.sleep(5)
