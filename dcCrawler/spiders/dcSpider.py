#!-*- coding:utf-8 -*-
import scrapy
import time
from urllib.parse import urlparse, parse_qs
from dcCrawler.items import DccrawlerItem

class dcCrawlerSpider(scrapy.Spider):
    name = "dcCrawler"
    def start_requests(self):
        for i in range(1):
            yield scrapy.Request(
                "https://gall.dcinside.com/board/lists/?id=leagueoflegends3&page={}".format(i+1), self.parse_url )

    def parse_url(self, response):
        for article in response.xpath('//*[@id="container"]/section[1]/article[2]/div[2]/table/tbody/tr/td[2]'):
            query = article.xpath("a[1]/@href").extract()[0]
            print (query)
            time.sleep(1)
            yield scrapy.Request(
                    response.urljoin(query), # article link
                    callback = self.parse_article
                )
        

    def parse_article(self, response):
        title = response.xpath('//*[@id="container"]/section/article[2]/div[1]/header/div/h3/span[2]/text()').extract() 
        _query = parse_qs( urlparse(response.url).query )
        _query['title'] = title

        data = {
            "id": _query['id'], "no": _query['no'], "cpage": _query['page'], "managerskill":"", "del_scope": "1", "csort": ""
            }
        yield scrapy.FormRequest(
            "https://m.dcinside.com/ajax/response-comment",
            formdata  = data, callback = self.parse_comment,
            cb_kwargs = _query
        )
    

    def parse_comment(self, response, id, no, page, title):
        print(id, no, title)
        print(response.xpath('/html/body/ul/li/p/text()').extract())
        
        