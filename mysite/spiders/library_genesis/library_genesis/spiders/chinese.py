# -*- coding: utf-8 -*-
import scrapy

from ..items import math
import copy


class MathSpider(scrapy.Spider):
    name = 'chinese'
    allowed_domains = ['libgen.is']
    start_urls = [
        'http://libgen.is/search.php?&res=100&req=chinese&phrase=1&view=detailed&column=language&sort=id&sortmode=DESC']

    def parse(self, response):
    #     for i in range(1, 10):
    #         yield scrapy.Request(
    #             url='https://libgen.lc/search.php?&res=100&req=Math&phrase=1&view=simple&column=def&sort=def&sortmode=ASC&page=' + str(
    #                 i)
    #             , callback=self.get_main)
    #
    # def get_main(self, response):
    #     print(response.body)  # test whether html text was got successfully
        book = math()  # 将信息存入LibraryGenesisItem对象

        book['title'] = response.xpath('//td[@colspan=2]/b')
        book['title'] = book['title'].xpath('string(.)').extract()
        # print(book['title'])  # for test suc

        book['author'] = response.xpath('//td[@colspan=3]/b')
        book['author'] = book['author'].xpath("string(.)").extract()
        # print(book['author'])  # for test suc

        book['publisher'] = response.xpath('//tr[@valign][position()=5]/td[2]').extract()
        for i in range(0, 100):
            book['publisher'][i] = book['publisher'][i].replace("<td>", '')
            book['publisher'][i] = book['publisher'][i].replace("</td>", ' ')
        # print(book['publisher'])  # for test

        book['year'] = response.xpath('//tr[@valign][position()=6]/td[2]').extract()
        for i in range(0, 100):
            book['year'][i] = book['year'][i].replace("<td>", '')
            book['year'][i] = book['year'][i].replace("</td>", ' ')
        # print(book['year'])  # for test

        book['url'] = response.xpath('//td[@colspan=2]/b/a/@href').extract()
        for i in range(0, 100):
            book['url'][i] = book['url'][i].replace("..", 'http://libgen.is')
        # print(book['url'])

        # print(book)
        books = math()
        for i in range(0, 100):
            books['title'] = book['title'][i]
            books['author'] = book['author'][i]
            books['publisher'] = book['publisher'][i]
            books['year'] = book['year'][i]
            books['url'] = book['url'][i]
            # print(books)
            # yield books
            yield scrapy.Request(url=book['url'][i], meta={'books': copy.deepcopy(books)}, callback=self.get_cover)

    def get_cover(self, response):
        books = response.meta['books']
        cover = response.xpath('//td/a/img/@src').extract_first()
        books['cover'] = "https://libgen.is" + cover
        books['type'] = 'chinese'
        books['website'] = 'libgen.is'
        # print(books)
        yield books

