#!-*- coding:utf-8 -*-
import scrapy
import time
from dcCrawler.items import DccrawlerItem

class dcCrawlerSpider(scrapy.Spider):
    name = "dcCrawler"
    # start_urls = [
    #     "https://gall.dcinside.com/board/lists/?id=leagueoflegends3&page={}",
    #     # "https://gall.dcinside.com/board/lists/?id=superidea"
    #     ]
    def start_requests(self):
        for i in range(2):
            yield scrapy.Request(
                "https://gall.dcinside.com/board/lists/?id=leagueoflegends3&page={}".format(i+1), self.parse_url )

    def parse_url(self, response):
        for article in response.xpath('//*[@id="container"]/section[1]/article[2]/div[2]/table/tbody/tr/td[2]'):
            link = article.xpath("a[1]/@href").extract()[0]
            print(response.urljoin(link))
            request = scrapy.Request(
                    response.urljoin(link), # article link
                    callback = self.parse_article
                )
            sleep(1)
            # print(article.xpath("a[2]/@href").extract()) # comment
            yield request

    def parse_article(self, response):
        title = response.xpath('//*[@id="container"]/section/article[2]/div[1]/header/div/h3/span[2]') 
        print(title)
