from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


def get_site(url: str) -> webdriver:
    driver = webdriver.Firefox()
    # driver = webdriver.Chrome()
    driver.get(url)
    return driver


def get_hillel(user: str = "guest", passw: str = "welcome2qauto"):
    return get_site(f"https://{user}:{passw}@qauto.forstudy.space/")


def find_element(driver, by, locator: str):
    try:
        element = driver.find_element(by, locator)
    except NoSuchElementException:
        print("element not found")
        return
    return element


def main_menu_about(driver):
    return find_element(driver, By.ID, "about")


def find_field(driver):
    return find_element(driver, By.XPATH, '//input[@type="search"]')


def not_found(driver):
    return find_element(driver, By.XPATH, '//ul[@class="list-recent-events menu"]/p')


def click(element):
    element.click()


def search_input(element, text: str):
    element.clear()
    element.send_keys(text)
    element.send_keys(Keys.RETURN)


def get_text(element):
    return element.text


if __name__ == "__main__":
    url = "http://www.python.org"
    driver = get_site(url)
    # driver = get_hillel(user="guest2", passw="new_pass")
    element = main_menu_about(driver)
    click(element)
