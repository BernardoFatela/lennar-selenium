# test_sign_up.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import pytest
import time
from helper_functions import click_element, input_text


def test_sign_up(setup,driver):
    wait = WebDriverWait(driver, 10)
    click_element(driver, "//button[@aria-label='open-panel']", "Open panel button not found or not clickable.")
    click_element(driver, "//a[@class='AuthMenuContent_authLink__lP2HC']", "'Sign in or create' link not found or not clickable.")
    click_element(driver, "//a[@href='https://stage.lennar.com/account/sign-up/']", "'Get Started' link not found or not clickable.")

    input_text(driver, "//input[@type='email']", "test@gmail.com", "Email input not found or not accessible.")
    time.sleep(1)

    click_element(driver, "//button[@aria-label='Continue']", "Continue button not found or not clickable.")

    input_text(driver, "//input[@name='password']", "test1234!", "Password input not found or not validating password properly.")
    input_text(driver, "//input[@name='confirmPassword']", "test1234!", "Password input not found or not validating password properly.")

    time.sleep(2)
    click_element(driver, "//button[@aria-label='Continue']", "Continue button not found or not clickable.")

    input_text(driver, "//input[@name='firstName']", "Lennar", "User details not working")
    input_text(driver, "//input[@name='lastName']", "Company", "User details not working")
    input_text(driver, "//input[@name='phone']", "5213321232", "User details not working")

    #dropdown
    dropdown_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='FormDropdown_root__U2og8']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", dropdown_element)
    dropdown_element.click()
    
    #click an element in dropdown
    div_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'MPCHoursDropdown_optionWrapper__ENXeX')]//span[text()='United States +1']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", div_element)

    # Click the div element
    div_element.click()

    click_element(driver, "//button[@aria-label='Continue']", "Continue button not found or not clickable.")
    
    dropdown_elements = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='FormDropdown_root__U2og8']")))
    dropdown_element = dropdown_elements[1]
    driver.execute_script("arguments[0].scrollIntoView(true);", dropdown_element)
    dropdown_element.click()
    parent_div = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Alabama')]/ancestor::div[@class='MPCHoursDropdown_optionWrapper__ENXeX']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", parent_div)
    parent_div.click()
    click_element(driver, "//button[@aria-label='Create account']", "Create account button not found or not clickable.")
    