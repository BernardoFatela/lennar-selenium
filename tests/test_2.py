# test_sign_up.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import pytest
import time
from helper_functions import login


def test_sign_in(setup,driver):
    login(driver, "test@gmail.com", "test1234!")