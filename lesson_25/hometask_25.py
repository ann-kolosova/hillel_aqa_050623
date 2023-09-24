"""Hometask_25. Locators."""


import sys
from pathlib import Path

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# find logger module
logger_file = Path(__file__).parent.parent / 'lesson_23'
sys.path.insert(0, str(logger_file))
from logger import logger


def get_site(url: str) -> webdriver:
    """Open browser with url."""
    driver = webdriver.Firefox()
    driver.get(url)
    return driver


def find_element(driver, by, locator: str):
    """Error when element not found."""
    try:
        element = driver.find_element(by, locator)
    except NoSuchElementException:
        logger.error('Element NOT found')
        return
    return element


def find_search_tracker(driver):
    """Find search field."""
    return find_element(driver, By.ID, 'en')


def find_search_button(driver):
    """Find search button."""
    return find_element(driver, By.ID, 'np-number-input-desktop-btn-search-en')


def click(element):
    """Click element."""
    element.click()


def search_ttn(element, text: str):
    """Input data."""
    element.clear()
    element.send_keys(text)


def error_message_main_page(driver):
    """Find error id section."""
    return find_element(driver, By.ID, 'np-number-input-desktop-message-error-message')


def get_text(element):
    """Get text."""
    return element.text


def wait_element(driver):
    """Adjust the timeout as needed."""
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="header__status-text"]')))
    return element
