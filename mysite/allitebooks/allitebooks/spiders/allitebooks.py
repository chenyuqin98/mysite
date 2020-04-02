import scrapy


class BookInfoSpider(scrapy.Spider):
    name = "bookinfo"
    allowed_domains = ["allitebooks.com", "amazon.com"]
    start_urls = [
        "http://www.allitebooks.com/security/",
    ]

    def parse(self, response):
        # response.xpath('//a[contains(@title, "Last Page →")]/@href').re(r'(\d+)')[0]
        num_pages = int(response.xpath('//a[contains(@title, "Last Page →")]/text()').extract_first())
        base_url = "http://www.allitebooks.com/security/page/{0}/"
        for page in range(1, num_pages):
            yield scrapy.Request(base_url.format(page), dont_filter=True, callback=self.parse_page)

    def parse_page(self, response):
        for sel in response.xpath('//div/article'):
            book_detail_url = sel.xpath('div/header/h2/a/@href').extract_first()
            yield scrapy.Request(book_detail_url, callback=self.parse_book_info)

    def parse_book_info(self, response):
        title = response.css('.single-title').xpath('text()').extract_first()