from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def save_and_refresh_page(self):
        pass