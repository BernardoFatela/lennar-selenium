# helper_functions.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import pytest
import time

def click_element(driver, xpath, error_message):
    try:
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()
    except (NoSuchElementException, TimeoutException):
        pytest.fail(error_message)

def click_element_when_visible(driver, xpath, error_message):
    try:
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        element.click()
    except (NoSuchElementException, TimeoutException):
        pytest.fail(error_message)

def input_text(driver, xpath, text, error_message):
    try:
        wait = WebDriverWait(driver, 10)
        input_field = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        input_field.send_keys(text)
    except (NoSuchElementException, TimeoutException):
        pytest.fail(error_message)

def login(driver, email, password):
    click_element(driver, "//button[@aria-label='open-panel']", "Open panel button not found or not clickable.")
    time.sleep(3)
    click_element(driver, "//a[@class='AuthMenuContent_authLink__lP2HC']", "'Sign in or create' link not found or not clickable.")
    time.sleep(3)
    input_text(driver, "//input[@type='email']", email, "Error related to email insertion.")
    time.sleep(3)
    click_element(driver, "//button[contains(@class, 'continue-button')]", "Continue button not found or not clickable.")
    time.sleep(3)
    input_text(driver, "//input[@type='password']", password, "Could not sign in after inputing password.")
    click_element(driver, "//button[contains(@class, 'continue-button')]", "Continue button not found or not clickable.")

