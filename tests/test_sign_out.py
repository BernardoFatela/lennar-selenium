# test_sign_up.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import pytest
import time

#signs_in and then out
def test_sign_out(setup,driver):
    wait = WebDriverWait(driver, 10)
    # Click on the button to open the panel
    try:
        open_panel_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='open-panel']"))
        )
        open_panel_button.click()
    except (NoSuchElementException, TimeoutException):
        pytest.fail("Open panel button not found or not clickable.")

    # Wait until the "Sign in or create" link is visible
    try:
        sign_in_link = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//a[@class='AuthMenuContent_authLink__lP2HC']"))
        )
        sign_in_link.click()
    except (NoSuchElementException, TimeoutException):
        pytest.fail("'Sign in or create' link not found or not clickable.")

    #new page email_input
    try:    
        email_input = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))
        )
        email_input.send_keys("test@gmail.com")
        continue_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'continue-button')]"))
        )
        continue_button.click()
    except (NoSuchElementException, TimeoutException):
        pytest.fail("Error related to email insertion")

    #new page password_input
    try:    
        password_input = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='password']"))
        )
        password_input.send_keys("test1234!")
        continue_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'continue-button')]"))
        )
        continue_button.click()
    except (NoSuchElementException, TimeoutException):
        pytest.fail("Could not sign in after inputing password.")

    #end of sign in
    # Click on the button to open the panel
    try:
        log_out_button = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='Log out']"))
        )
        log_out_button.click()
    except (NoSuchElementException, TimeoutException):
        pytest.fail("'Sign in or create' link not found or not clickable.")
    