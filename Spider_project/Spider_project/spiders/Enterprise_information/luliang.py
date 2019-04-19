# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
import re

class LuliangSpider(CrawlSpider):
    name = 'luliang'
    # allowed_domains =[]# ['qichacha.com']
    start_urls = ['https://xin.demlution.com/app-company/search-province-%E5%8C%97%E4%BA%AC%E5%B8%82.html?province=%E5%8C%97%E4%BA%AC%E5%B8%82&offset=10']

    page_lian = LinkExtractor(restrict_xpaths="//section[3]//ul[@class='pager']/li[@class='next']/a")
    xiang_xi=LinkExtractor(restrict_xpaths="//div[@class='b-item clearfix']//a[@class='b-item-name']")
    rules = [
        Rule(page_lian, follow=True),
        Rule(xiang_xi, follow=False, callback='parse_item')
    ]

    def parse_item(self, response):

        name=response.xpath("string(//table[@class='table-top table']//tr[1]/td[@class='b-t-value'][2])").extract_first()
        faren=response.xpath("string(//table[@class='table-top table']//tr[2]/td[@class='b-t-value b-t-name'])").extract_first()
        shijian=response.xpath("string(//table[@class='table-top table']//tr[3]/td[@class='b-t-value'][2])").extract_first()
        jiezhi=response.xpath("string(//table[@class='table-top table']//tr[4]/td[@class='b-t-value'][2])").extract_first()
        hezhunri=response.xpath("string(//table[@class='table-top table']//tr[5]/td[@class='b-t-value'][2])").extract_first()
        fari=response.xpath("string(//table[@class='table-top table']//tr[6]/td[@class='b-t-value'][2])").extract_first()
        # print(response.url,name,faren,shijian,jiezhi,hezhunri,fari)


        hao = response.xpath("string(//table[@class='table-top table']//tr[1]/td[@class='b-t-value'][1])").extract_first()
        lei=response.xpath("string(//table[@class='table-top table']//tr[2]/td[@class='b-t-value'][1])").extract_first()
        ziben=response.xpath("string(//table[@class='table-top table']//tr[3]/td[@class='b-t-value'][1])").extract_first()
        jing = response.xpath("string(//table[@class='table-top table']//tr[4]/td[@class='b-t-value'][1])").extract_first()
        dengji = response.xpath("string(//table[@class='table-top table']//tr[5]/td[@class='b-t-value'][1])").extract_first()
        zhuangtai = response.xpath("string(//table[@class='table-top table']//tr[6]/td[@class='b-t-value'][1])").extract_first()
        zhucedi= response.xpath("string(//table[@class='table-bottom']//tr[1]/td[@class='b-t-value b-t-w'])").extract_first()
        # print(response.url,hao,lei,ziben,jing,dengji,zhuangtai,zhucedi)





        # aa=re.findall('企业名称：(.*?)类型：',response.text,re.S)[0]
        # zui=re.findall('<td class="b-t-value">(.*?)<\/td>',aa,re.S)[0]
        # print(zui)







