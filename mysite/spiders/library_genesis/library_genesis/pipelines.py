# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class LibraryGenesisPipeline(object):
    def __init__(self):
        # 建立数据库连接
        self.connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='mysite',
                                          charset='utf8')
        # 创建操作游标
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        # 定义sql语句
        sql = """
            insert into wx_books(type,title,website,author,publisher,year,url,cover)
            values(%s,%s,%s,%s,%s,%s,%s,%s)
        """
        # 执行sql语句
        self.cursor.execute(sql,(item['type'],item['title'],item['website'],item['author'],item['publisher'],item['year'],item['url'],item['cover']))
        # 保存修改
        self.connection.commit()
        return item

    def __del__(self):
        # 关闭操作游标
        self.cursor.close()
        # 关闭数据库连接
        self.connection.close()
