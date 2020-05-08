# -*- coding: utf-8 -*-
import scrapy

from ..items import math, type
import copy


class MathSpider(scrapy.Spider):
    name = 'douban'
    # allowed_domains = ['book.douban']
    start_urls = [
        'https://book.douban.com/tag/']

    def parse(self, response):
        types = type()
        types['type'] = response.xpath('//td/a')
        types['type'] = types['type'].xpath("string(.)").extract()
        # print(types['type'])
        book_type = math()
        for i in range(0, 2):
            book_type['type'] = types['type'][i]
            # print(book_type)
            yield scrapy.Request(url='https://book.douban.com/tag/' + str(book_type['type']),
                                 meta={'types': copy.deepcopy(book_type)}, callback=self.get_main)

    def get_main(self, response):
        type = response.meta['types']
        # print(type['type'])
        # print(response.body)  # test whether html text was got successfully
        books = math()  # 将信息存入LibraryGenesisItem对象
        books['url'] = response.xpath('//h2/a/@href').extract()

        book_info = response.xpath('//div[@class="info"]/div[1]').extract()
        book = math()
        for i in range(0,20):
            book_info[i] = book_info[i].replace("\n", "")
            book_info[i] = book_info[i].replace(" ", "")
            book_info[i] = book_info[i].replace("</div>", "")
            book_info[i] = book_info[i].replace('<divclass="pub">', "")

            book['publisher']=book_info[i].split('/')[-3]
            book['year']=book_info[i].split('/')[-2]
            book['type'] = type['type']
            book['url'] = books['url'][i]
            # print(book)
            yield scrapy.Request(url=books['url'][i], meta={'book': copy.deepcopy(book)}, callback=self.get_detail)

    def get_detail(self, response):
        book = response.meta['book']
        # print(book)
        book['title'] = response.xpath('//h1/span')
        book['title'] = book['title'].xpath('string(.)').extract_first()
        # print(book)  # for test suc

        book['author'] = response.xpath('//div[@id="info"]//a')
        book['author'] = book['author'].xpath("string(.)").extract_first()
        book['author'] = book['author'].replace("\n","")
        book['author'] = book['author'].replace(" ", "")

        book['cover'] = response.xpath("//div[@id='mainpic']/a/img/@src").extract_first()

        # book['introduce'] = response.xpath("//div[@class='intro']/p").extract_first()
        # book['introduce'] = book['introduce'].replace('<div class="intro">\n', "")
        # book['introduce'] = book['introduce'].replace("<p>", "")
        # book['introduce'] = book['introduce'].replace("</p>", "")
        # book['introduce'] = book['introduce'].replace("</div>", "")
        # book['introduce'] = book['introduce'].replace('''<a href="javascript:void(0)" class="j a_show_full">(
        # 展开全部)</a>''', "")
        divs = response.xpath("//div[@class='intro']")
        introduce = ""
        for p in divs.xpath('.//p/text()'):
            introduce = introduce + p.extract().strip()
            book['introduce'] = introduce

        # print(book)  # for test suc

        book['website'] = '豆瓣'
        print(book)
        yield book
