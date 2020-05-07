# -*- coding: utf-8 -*-
import scrapy

from ..items import math
import copy

class PhysicsSpider(scrapy.Spider):
    name = 'physics'
    allowed_domains = ['libgen.lc']
    start_urls = ['https://libgen.lc/search.php?req=Physics&open=0&res=100&view=simple&phrase=1&column=def']

    def parse(self, response):
        for i in range(1, 10):
            yield scrapy.Request(
                url='https://libgen.lc/search.php?&res=100&req=Physics&phrase=1&view=simple&column=def&sort=def&sortmode=ASC&page=' + str(
                    i)
                , callback=self.get_main)

    def get_main(self, response):
        # print(response.body)  # test whether html text was got successfully
        book = math()  # 将信息存入LibraryGenesisItem对象

        book['title'] = response.xpath('//td[@width]/a[@title]')
        book['title'] = book['title'].xpath('string(.)').extract()
        # print(book['title'])  # for test suc

        # book['author'] = response.xpath('//tr[@valign][position()>1]/td[2]|/a/text()').extract() #unknown error
        book['author'] = response.xpath('//tr[@valign][position()>1]/td[2]')
        book['author'] = book['author'].xpath("string(.)").extract()
        # print(book['author'])  # for test suc

        book['publisher'] = response.xpath('//tr[@valign][position()>1]/td[4]').extract()
        for i in range(0, 100):
            book['publisher'][i] = book['publisher'][i].replace("<td>", '')
            book['publisher'][i] = book['publisher'][i].replace("</td>", ' ')
        # print(book['publisher'])  # for test

        book['year'] = response.xpath('//tr[@valign][position()>1]/td[5]').extract()
        for i in range(0, 100):
            book['year'][i] = book['year'][i].replace("<td nowrap>", '')
            book['year'][i] = book['year'][i].replace("</td>", ' ')
        # print(book['year'])  # for test

        book['url'] = response.xpath('//table[@border]//tr/td[position()=1]/b/a/@href').extract()
        # print(book['url'])

        # print(book)
        books = math()
        for i in range(0,100):
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
        cover=response.xpath('//td/img/@src').extract_first()
        books['cover']="https://libgen.lc"+cover
        books['type']='physics'
        books['website']='libgen.lc'
        print(books)
        yield books

