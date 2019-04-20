# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import InformationItem
import re
from scrapy import selector
import time
from copy import deepcopy

class FinanceSpider(CrawlSpider):
    name = 'finance'
    allowed_domains = ['www.financeun.com']
    start_urls = ['http://www.financeun.com/']

    rules = (
        Rule(LinkExtractor(allow=r'http:\/\/www.financeun.com\/articleList\/\d+\.shtml'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'http:\/\/www.financeun.com\/newsDetail\/\d+\.shtml\?platForm\=jrw'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        # 查看当前页面内容
        current_url = response.url
        # print(current_url)
        # 加入selector选择器
        # selecting = selector(response)
        detail_url_list = []
        if 'platForm=jrw' not in current_url:
            # 获取第一条新闻url
            firest_url = response.urljoin(response.xpath('/html/body/div[2]/div[1]/div[1]/a/@href').get())
            detail_url_list.append(firest_url)

            div_list = response.xpath('/html/body/div[2]/div[1]/div[2]/div')[:-2]
            for divs in div_list:

                item = InformationItem()
                try:
                    item['fb_time'] = divs.xpath('./div[1]/text()').get()[:-4]
                except:
                    item['fb_time'] = '空'
                try:
                    item['title'] = divs.xpath('./a/text()').get()
                except:
                    item['title'] = '空'
                try:
                    item['daodu'] = divs.xpath('./div[2]/text()').get().strip()
                except:
                    item['daodu'] = '空'
                try:
                    item['detail_url'] = response.urljoin(divs.xpath('./a/@href').get())
                    detail_url_list.append(item['detail_url'])
                except:
                    item['detail_url'] = '空'


                print(item['fb_time'])
                print(item['title'])
                print(item['daodu'])
                print(item['detail_url'])

        for detail_url in detail_url_list:
            yield scrapy.Request(url=detail_url,callback=self.parse_details,meta={'item':deepcopy(item)})


    def parse_details(self,response):
        print('=================进入详情页======================')
        # 接收item
        item = response.meta['item']
        response_data = response.body.decode('utf-8')
        # print(response_data)
        # print(current_url)

        laiyuan = re.findall("来源(.*)字号",response_data)[0].split(' ')[0][3:]
        # print(type(laiyuan))
        print(laiyuan)
        # laiyuan = selecting.css('div.navbar ::text')
        if laiyuan !=None:
            item['laiyuan'] = laiyuan
        else:
            item['laiyuan'] = '空'

        author = response.xpath('/html/body/div[2]/div[4]/div/div[7]/text()').get().strip()[5:]
        print(author)
        if author != None:
            item['author'] = author
        else:
            item['author'] = '空'

        item['yd_liang'] = '空'

        try:
            content = response.xpath('/html/body/div[2]/div[4]/div/div[6]//p/text()').getall()[0].strip()
        except:
            try:
                content = response.xpath('/html/body/div[2]/div[4]/div/div[6]/p/span/text()').get().strip()
            except:
                content = response.xpath('/html/body/div[2]/div[4]/div/div[6]/text()').get().strip()

        print(content)
        print(item['detail_url'])
        if content != None:
            item['content'] = content
        else:
            item['content'] = '空'


        guanjianzi = response.xpath('//*[@id="keywords1"]/text()').get()
        print(guanjianzi)
        if guanjianzi != None:
            item['guanjianzi'] = guanjianzi
        else:
            item['guanjianzi'] = '空'


        item['mz_shengming'] = '空'


        pq_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        print(pq_time)
        item['pq_time'] = pq_time

        item['fs_shu'] = '空'
        item['pl_shu'] = '空'
        try:
            peitu_url = response.urljoin(response.xpath('/html/body/div[2]/div[4]/div/div[6]//p/img/@src').get())
        except:
            peitu_url = '空'
        if peitu_url != None:
            item['peitu_url'] = peitu_url
        else:
            item['peitu_url'] = '空'

        item['kd_baokan'] = '空'


        weizhi = re.findall(r'<div class="navbar" style=".*?">\n\s+(.*?)\s\&gt;\&gt;\&gt;\s(.*?)\s+</div>',
                             response_data)

        complete_weizhi = weizhi[0][0] + '>>>' + weizhi[0][1]
        print(complete_weizhi)
        # laiyuan = selecting.css('div.navbar ::text')
        if laiyuan != None:
            item['weizhi'] = complete_weizhi
        else:
            item['weizhi'] = '空'