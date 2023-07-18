# test_sign_up.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import pytest
import time
from helper_functions import login,click_element_when_visible

#signs_in and then out
def test_sign_out(setup,driver):
    login(driver, "test@gmail.com", "test1234!")
    # Click on the button to open the panel
    click_element_when_visible(driver, "//button[@aria-label='Log out']", "'Log out' link not found or not clickable.")