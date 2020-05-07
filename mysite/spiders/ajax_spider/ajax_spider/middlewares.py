# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class AjaxSpiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class AjaxSpiderDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


from selenium import webdriver
import time
from scrapy.http import HtmlResponse


class SeleniumMiddleware(object):
    def __init__(self):
        # self.timeout = 50
        # # 2.Firefox---------------------------------
        # # 实例化参数对象
        # options = webdriver.FirefoxOptions()
        # # 无界面
        # # options.add_argument('--headless')
        # # 关闭浏览器弹窗
        # options.set_preference('dom.webnotifications.enabled', False)
        # options.set_preference('dom.push.enabled', False)
        # # 打开浏览器
        self.browser = webdriver.Chrome(
            executable_path="C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe")
        # 路径是chromedriver.exe的存放的位置
        # self.browser = webdriver.Firefox(firefox_options=options)
        # # 指定浏览器窗口大小
        # self.browser.set_window_size(1400, 700)
        # # 设置页面加载超时时间
        # self.browser.set_page_load_timeout(self.timeout)
        # self.wait = WebDriverWait(self.browser, self.timeout)

    def process_request(self, request, spider):
        # # 当请求的页面不是当前页面时
        # if self.browser.current_url != request.url:
        #     # 获取页面
        #     self.browser.get(request.url)
        #     time.sleep(5)
        # else:
        #     pass
        # # 返回页面的response
        self.browser.get("https://www.jiumodiary.com/")
        self.browser.find_element_by_xpath('//input[@id="SearchWord"]').send_keys("数学")
        self.browser.find_element_by_xpath('//button[@id="SearchButton"]').click()
        return HtmlResponse(url=self.browser.current_url, body=self.browser.page_source,
                            encoding="UTF-8", request=request)

    def spider_closed(self):
        # 爬虫结束 关闭窗口
        # self.browser.close()
        pass

    @classmethod
    def from_crawler(cls, crawler):
        # 设置爬虫结束的回调监听
        s = cls()
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s
