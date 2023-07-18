# test_search_home
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
import pytest
import time
from helper_functions import input_text,click_element


def test_search_home(setup,driver):
    input_text(driver, "//input[@id='search-field']", "Austin, Texas", "'Austin / Central Texas, TX area' link not found or not clickable.")
    time.sleep(3)
    click_element(driver, "//a[@data-testid='search-bar-result-cities-regions-0']", "'Austin / Central Texas, TX area' link not found or not clickable.")
    time.sleep(3)
    click_element(driver, "//button[@data-testid='search-results-filter-availability']", "'Availability' button not found or not clickable.")
    time.sleep(3)
    click_element(driver, "//div[@class='AvailabilityCheckbox_inputWrapper__FSw5R']", "'QuickMoveInHomes' checkbox not found or not clickable.")
    time.sleep(3)