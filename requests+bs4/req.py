# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
from bs4 import BeautifulSoup


#raw_cookies = """
#"""
#cookies = {}

headers = {
    "host":"movie.douban.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding":"Accept-Encoding",
}

base_url = "http://movie.douban.com/top250?start={page}&filter="

current_page = 0
step = 25
while current_page <= 250:
    url = base_url.format(page=current_page)
    current_page = current_page + step


    resp = requests.get(url, headers=headers)

    soup = BeautifulSoup(resp.text, "html5lib")
    for item in soup.select("ol li"):
        num = item.find("em").string
        rate = item.select(".rating_num")[0].string
        title = item.find("span").string
        print("No.{0}   [{1}]   {2}".format(num, rate, title))

