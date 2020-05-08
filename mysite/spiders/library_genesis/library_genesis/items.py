# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class math(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    type = scrapy.Field()  # 书籍类型 #
    title = scrapy.Field()  # 书籍标题（包含isbn） #
    website = scrapy.Field()  # 书籍的来源网站
    author = scrapy.Field()  # 书籍作者 #
    publisher = scrapy.Field()  # 出版社 #
    year = scrapy.Field()  # 出版时间 #
    url = scrapy.Field()  # 下载地址 #
    cover = scrapy.Field()  # 封面图片地址 #
    introduce = scrapy.Field()


class type(scrapy.Item):
    type = scrapy.Field()  # 书籍类型
