import requests
from lxml import html

url = "https://www.babyshop.com/"


def get_site(url: str):
    return requests.get(url).content  # повертає сайт як строку


def find_element(xpath: str):
    content = get_site(url)
    tree = html.fromstring(content) # будує віртуальне дерево елементів із html
    try:
        element = tree.xpath(xpath)[0]
    except IndexError:
        print("WARNING: element not found") # logger !!
        return
    return element

if __name__ == "__main__":
    left_main_menu = '//button[@class="pl-5 pr-3"]'
    menu = find_element(left_main_menu)
    if menu is not None:
        print(menu.attrib, menu.text)
    search_item = '//*[@placeholder="Search"]'
    menu = find_element(search_item)
    if menu is not None:
        print(menu.attrib, menu.text)
    basket_item = '//button[@aria-label="open cart"]'
    menu = find_element(basket_item)
    if menu is not None:
        print(menu.attrib, menu.text)
