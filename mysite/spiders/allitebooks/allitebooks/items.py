# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    title = scrapy.Field()
    isbn = scrapy.Field()
    price = scrapy.Field()


class allitbooks(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    type = scrapy.Field()
    title = scrapy.Field()
    website = scrapy.Field()
    author = scrapy.Field()
    publisher = scrapy.Field()
    year = scrapy.Field()
    url = scrapy.Field()
    cover = scrapy.Field()
