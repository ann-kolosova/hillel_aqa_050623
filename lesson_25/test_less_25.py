from lesson_25 import get_site, main_menu_about, click
from lesson_25 import find_field, not_found, search_input, get_text
from time import sleep


def test_menu():
    url = "https://www.python.org"
    driver = get_site(url)
    element = main_menu_about(driver)
    assert element is not None, "element not found"
    click(element)
    assert driver.current_url == url+"/about/"


def test_search():
    url = "https://www.python.org"
    driver = get_site(url)
    element = find_field(driver)
    assert element is not None, "element not found"
    search_input(element, "python")
    sleep(0.5)
    element = not_found(driver)
    text = get_text(element)
    assert text != "No results found.", "Search doesn't work"
