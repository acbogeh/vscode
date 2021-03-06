from bs4 import BeautifulSoup
from html.parser import HTMLParser
#from html5lib import html5parser
import io
import sys
import re
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


soup = BeautifulSoup (html_doc,"html.parser",from_encoding=None)
print('获取所有链接')
links = soup.find_all('a')
for link in links:
    print(link.name,link['href'],link.get_text())
print('获取lacie')
linkslacie = soup.find('a',href='http://example.com/lacie')
print(linkslacie.name,linkslacie['href'],linkslacie.get_text())
print('正则表达式匹配')
linksre = soup.find('a',href = re.compile(r'll'))
print(linksre.name,linksre['href'],linksre.get_text())
print('获取p段落')
linkp = soup.find('p',class_ = 'title')
print(linkp.name,linkp.get_text())