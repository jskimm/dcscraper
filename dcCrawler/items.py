# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DccrawlerItem(scrapy.Item):
    id = scrapy.Field()
    no = scrapy.Field()
    title = scrapy.Field()
    comments = scrapy.Field()
