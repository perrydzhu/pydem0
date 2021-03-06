import requests
from lxml import etree
import lxml.html


class BookSpider(object):

    def __init__(self):
        # （1）初始化设置

        self.url_tpl = "https://read.douban.com/kind/100?start={}&sort=hot&promotion_only=False&min_price=None&max_price=None&works_type=None"

    def crawl(self):
        # （2）爬取get请求页面的内容
        try:
            r = requests.get(self.url_tpl, timeout=15)
            if r.status_code == 200:
                for page in range(5):
                    linkAdress = requests.get(self.url_tpl.format(page * 20), timeout=20)
                    linkAdress.encoding = "utf-8"
                    linkContent = etree.HTML(linkAdress.text)
                    # print(linkContent.xpath('//div[@class="title"]/a/text()'))
                    # print(linkContent.xpath('//div[@class="title"]/p/text()'))
                    print(linkContent.xpath('//div[@class="article-desc-brief"]/text()'))
            else:
                r.raise_for_status
                print('Failed to get the link:', self.url_tpl)

        except Exception as e:
            raise e
        return r.text

    def crawl2(self):
        try:
            req = requests.get(self.url_tpl)
            if req.status_code == 200:
                for page in range(1):
                    response = requests.get(self.url_tpl.format(page * 20))
                    response.encoding = "utf-8"
                    html = lxml.html.fromstring(response.text)
                    booklist = html.xpath('//ul[@class="list-lined ebook-list column-list"]/li')
                    print(len(booklist))
                    for book in booklist:
                        # title = book.xpath('.//div[@class="title"]/a/text()')[0].text_content()
                        title = book.xpath('.//div[@class="title"]/a/text()')[0]
                        rating_element = book.xpath('.//span[@class="rating-average"]')
                        if len(rating_element):
                            rating = rating_element[0].text_content()
                        else:
                            rating = 0

                        # comments = book.xpath('.//div[@class="article-desc-brief"]')[0].text_content()
                        comments = book.xpath('//div[@class="article-desc-brief"]/text()')[0]

                        author = book.xpath('.//a[@class="author-item"]')[0].text_content()
                        output = "<<{}>>, {}, {}, {}"
                        print(output.format(title, rating, author, comments))

            else:
                print('Failed to get the link:', self.url_tpl)

        except Exception as e:
            print("Error happened")
            print(e)


if __name__ == "__main__":
    analysis_new = BookSpider()
    # analysis_new.crawl()
    analysis_new.crawl2()
