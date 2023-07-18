# test_search_home
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
import pytest
import time


def test_search_home(setup,driver):
    wait = WebDriverWait(driver,10)
    try:
        address_input = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='search-field']"))
        )
        address_input.send_keys("Austin, Texas")
        address_input.send_keys(Keys.RETURN)
    except (NoSuchElementException, TimeoutException):
        pytest.fail("'Austin / Central Texas, TX area' link not found or not clickable.")
    try:
        link = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//a[@data-testid='search-bar-result-cities-regions-0']"))
        )
        link.click()
    except (NoSuchElementException, TimeoutException):
        pytest.fail("'Austin / Central Texas, TX area' link not found or not clickable.")
    
    try:
        button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='search-results-filter-availability']"))
        )
        button.click()
    except (NoSuchElementException, TimeoutException):
        pytest.fail("'Availability' button not found or not clickable.")
#dropdown is clicked and now we select element

    try:
        checkbox = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='AvailabilityCheckbox_inputWrapper__FSw5R']"))
        )
        checkbox.click()
    except (NoSuchElementException, TimeoutException):
        pytest.fail("'QuickMoveInHomes' checkbox not found or not clickable.")