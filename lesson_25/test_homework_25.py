"""
Написати тест, що вводить трекінг посилки на сайті НП.

https://tracking.novaposhta.ua/#/uk/
та отримує статус посилки  в теркінгу, напр.
<div data-v-631babf2="" class="header__parcel-dynamic-status px-4 d-flex align-center">
<div data-v-631babf2="" class="d-flex flex-column status-icon mr-4 status-icon-grey">
<!----></div>
<div data-v-631babf2="" class="flex-grow-1"
<div data-v-631babf2="" class="header__status-header"> Зараз: </div><!---->
<div data-v-631babf2="" class="header__status-text"> Посилка отримана </div>
</div></div>
== Посилка отримана
"""

from hometask_25 import click, error_message_main_page, find_search_button
from hometask_25 import find_search_tracker, get_site, get_text
from hometask_25 import search_ttn, wait_element


def test_search_tracking():
    """Find & click on search."""
    url = 'https://tracking.novaposhta.ua/#/uk/'
    driver = get_site(url)
    element = find_search_tracker(driver)
    assert element is not None, 'element not found'
    click(element)
    assert driver.current_url == url, 'incorrect url'
    driver.close()


def test_find_search_button():
    """Find & click on button 'Пошук'."""
    url = 'https://tracking.novaposhta.ua/#/uk/'
    driver = get_site(url)
    element = find_search_tracker(driver)
    click(element)
    element = find_search_button(driver)
    assert element is not None, 'element NOT found'
    click(element)
    assert driver.current_url == url, 'incorrect url'
    driver.close()


def test_received():
    """Case for received parcel."""
    url = 'https://tracking.novaposhta.ua/#/uk/'
    driver = get_site(url)
    element = find_search_tracker(driver)
    click(element)
    ttn = '20400350602119'
    search_ttn(element, ttn)
    element = find_search_button(driver)
    click(element)
    element = wait_element(driver)
    text = get_text(element)
    assert text == 'Отримана', 'element NOT found'
    driver.close()


def test_not_exist_ttn():
    """Parcel not found."""
    url = 'https://tracking.novaposhta.ua/#/uk/'
    driver = get_site(url)
    element = find_search_tracker(driver)
    click(element)
    ttn2 = '2070048542856'
    search_ttn(element, ttn2)
    element = find_search_button(driver)
    click(element)
    element = error_message_main_page
    assert element is not None, 'element NOT found'
    driver.close()
