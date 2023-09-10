import lxml.html
from lxml.html import fromstring, fragment_fromstring
from lxml import etree
from io import StringIO

broken_html = """<html><head>
<title>test<body><h1>page title</h3>
<a rel='my@mail.com'>click me</a>
<p class='abc' > some text
<div id="xyz"> text </div>
""" # неевірний покоцаний хтмл

parser = etree.HTMLParser()  # наслідуєм клас хтмл парсер
read_html = StringIO(broken_html)
tree = etree.parse(read_html, parser) # перетворюєм в зрозумілу структуру
result = etree.tostring(tree.getroot(),
    pretty_print=True, method="html")  # звороне перетворення - обєкт дерева у строку
print(result)

tree = lxml.html.fromstring(result)
result = tree.find_class("abc")
print(result[0].attrib, result[0].text)

result2 = tree.find_rel_links("my@mail.com")
print(result2[0].attrib, result2[0].text)

result3 = tree.get_element_by_id("xyz")
print(result3.attrib, result3.text)


