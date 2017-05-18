# -*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup

http_pattern = re.compile(
    r'('  # match group
    r'(?:http|ftp)s?://'  # match 'http://', 'https://', 'ftp://'
    r'(?:(?:[A-Z0-9]+\.)+)?'  # match 'www.aaa.', 'weibo.', '192.168.', or nothing
    r'(?:[A-Z0-9]+\.[A-Z0-9]+)'  # match 'abc.com', '23.254'
    r'(?::\d{2,5})?'  # match port
    r')'
    , re.IGNORECASE)

url = "http://www.baidu.com"
url = "http://www.nuomi.com"
url = "http://www.taobao.com"

next_url = []

r = requests.get(url)

print r.status_code

html = BeautifulSoup(r.content, "html5lib")

#print html.prettify()

for link in html.find_all('a'):
    url = link.get('href')
    if url:
        matched = http_pattern.match(url)
    if matched:
        m = matched.group(1)
        if m not in next_url:
            next_url.append(m)

print next_url
