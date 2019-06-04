from scrapy.spiders import CrawlSpider
from bs4 import BeautifulSoup
from scrapy_splash import SplashRequest
from hexun.items import HexunItem


class HexunSpider(CrawlSpider):
    name = 'hexun'
    start_urls = ['http://forex.hexun.com/rmbhl']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        soup = BeautifulSoup(response.body, "html.parser")
        td_list = soup.body.find(id='BankNameList').find_all('td', class_='fir_td')
        for td in td_list:
            item = HexunItem()
            print(td.div.string.strip())
            print(td.find(class_='pere').em.string.strip())
            result = td.div.string.strip().split('/')
            item['from_currency'] = result[0]
            item['to_currency'] = result[1]
            item['rate'] = td.find(class_='pere').em.string.strip()
            yield item


