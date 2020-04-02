# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from scrapy.selector import Selector


#知乎的模拟登录
browser = webdriver.Chrome(executable_path="C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe")  #路径是chromedriver.exe的存放的位置
# browser.get("https://www.zhihu.com/#signin")
browser.get("https://www.jiumodiary.com/")
time.sleep(3)
browser.find_element_by_xpath('//input[@id="SearchWord"]').send_keys("数学")
time.sleep(2)
browser.find_element_by_xpath('//button[@id="SearchButton"]').click()
time.sleep(3)
elem = browser.find_element_by_xpath("//*")
source_code = elem.get_attribute("innerHTML")
print(source_code)
# browser.find_element_by_css_selector(".view-signin input[name='account']").send_keys("********") #帐号
# browser.find_element_by_css_selector(".view-signin input[name='password']").send_keys("********") #密码
# browser.find_element_by_id("captcha").send_keys(input('请输入验证码：'))
# browser.find_element_by_css_selector(".view-signin button.sign-button").click() #登录
# browser.quit()


#可以用selenium得到js加载后的html，比如这样的话可以抓取到本来抓取的不到的一些字段（淘宝的交易量等等）
# browser = webdriver.Chrome(executable_path="E:/chromedriver.exe")
# browser.get("https://detail.tmall.com/item.htm?spm=a230r.1.14.3.yYBVG6&id=538286972599&cm_id=140105335569ed55e27b&abbucket=15&sku_properties=10004:709990523;5919063:6536025")
# print(browser.page_source) #page_source就是js加载完的源代码
# browser.close() #关闭窗口
# browser.quit() #关闭窗口并退出
'''
如果是用selenium本身的选择器（python写的，比较慢），会很慢
所以现在转换成scrapy中的selector（他是用c语言写的，很快）
模版，也可以嵌入scrapy中
'''
# t_selector=Selector(text=browser.page_source)
# print(t_selector.xpath('//*[@id="J_StrPriceModBox"]/dd/span/text()').extract())