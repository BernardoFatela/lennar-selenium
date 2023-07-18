import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


@pytest.fixture(scope="function")
def driver():
    # Set up the driver
    driver = webdriver.Firefox()  # or webdriver.Chrome(), depending on your browser
    yield driver  # Yield the driver object to make it available to the tests

    # Clean up
    driver.quit()


@pytest.fixture(scope="function")
def setup(driver):
    driver.get("https://stage.lennar.com/")

    wait = WebDriverWait(driver, 10)

    # Cookies button
    try:
        # Wait until the accept cookies button is present on the page
        accept_button = wait.until(
            EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
        )

        # Click the accept button
        accept_button.click()

        wait.until(
            EC.invisibility_of_element_located((By.ID, "onetrust-accept-btn-handler"))
        )
    except (NoSuchElementException, TimeoutException):
        print("First accept button not found or not clickable.")

    try:
        # Wait until the second accept button is present on the page

        second_accept_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@data-testid='cookie-notice-accept']")
            )
        )

        # Click the second accept button
        second_accept_button.click()

    except (NoSuchElementException, TimeoutException):
        print("Second accept button not found or not clickable.")

    i = 0

    try:
        # National Events Close
        close_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(@class, 'TakeOverModalV2_closeIcon__xfk_B')]",
                )
            )
        )

        # Click the close button
        close_button.click()

        # wait for the pop up of the event to close
        wait.until(
            EC.invisibility_of_element_located((By.ID, "onetrust-accept-btn-handler"))
        )
    except NoSuchElementException:
        print("National Sales Event close button not clickable")
