# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class Zhengfuxinxi20190319Pipeline(object):
    def __init__(self):
        self.connect = pymysql.Connect('127.0.0.1', 'root', '123')
        self.cur = self.connect.cursor()
        self.cur.execute('use zhengfuxinxi;')
        try:
            self.cur.execute('drop table zhengfuxinxi;')
        except Exception as e:
            pass

        self.cur.execute(
                'create table zhengfuxinxi(id int primary key auto_increment, code varchar(50),info varchar (1000),maker varchar (100));')

    def process_item(self, item, spider):
        self.cur.execute(
            'insert zhengfuxinxi values (0,"%s","%s","%s")' % (item['code'], item['info'], item['maker']))
        self.connect.commit()
        return item

    def close_spider(self,item,spider):
        self.connect.close()
