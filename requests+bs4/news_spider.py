import requests
import lxml.html

url = "http://tech.163.com/16/0809/00/BU034L0B00097U7R.html"

browser = requests.get(url)

root = lxml.html.fromstring(browser.text)

content = root.xpath('//div[@id="epContentLeft"]')[0]

title = content.xpath('./h1')[0].text_content()
source = content.xpath('./div[@class="post_time_source"]')[0].text_content().strip()
print(title)
print(source)

