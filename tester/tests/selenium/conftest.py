import pytest
import os
from selenium import webdriver
from config import *
from locators import *

EMAIL, PASSWORD = os.getenv('EMAIL'), os.getenv('PASSWORD')

#TODO explicit_wait
@pytest.fixture
def set_webdriver():
    driver = webdriver.Chrome(CHROMEDRIVER_PATH)
    driver.get(URL)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def authentification(driver):
    if driver.is_present(AuthPageLocators.EMAIL):
        driver.find_element(AuthPageLocators.EMAIL).send_keys(EMAIL)
    if driver.is_present(AuthPageLocators.PASSWORD):
        driver.find_element(AuthPageLocators.PASSWORD).send_keys(PASSWORD)
    if driver.is_clickable(AuthPageLocators.SUBMIT_BUTTON):
        driver.find_element(AuthPageLocators.SUBMIT_BUTTON).click(AuthPageLocators.SUBMIT_BUTTON)
