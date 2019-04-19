# -*- coding: utf-8 -*-
import scrapy
from ..items import Zhengfuxinxi20190319Item

class ZhengfuSpider(scrapy.Spider):
    name = 'zhengfu'
    # allowed_domains = ['xxx']
    start_urls = []
    for page in range(1,6):
        url = 'http://www.cnnvd.org.cn/web/vulnerability/querylist.tag?pageno='+str(page)+'&repairLd='
        start_urls.append(url)

    def parse(self, response):
        datalist = response.xpath("//div[@class='list_list']/ul/li")
        for i in datalist:
            url = 'http://www.cnnvd.org.cn' + i.xpath("./div/a[@class='a_title2']/@href").extract()[0]
            yield scrapy.Request(url=url,callback=self.parse_content)

    def parse_content(self, response):

        code = response.xpath("//div[@class='detail_xq w770']/ul/li[1]/span/text()").extract()[0]
        info = ''.join(response.xpath("//div[@class='fl w770']/div[@class='d_ldjj']//text()").extract())
        maker = response.xpath("//div[@class='fl w770']/div[@class='detail_xq w770']/ul/li[8]/span/text()").extract()[0]
        item = Zhengfuxinxi20190319Item()
        item['code'] = code
        item['info'] = info
        item['maker'] = maker
        yield item
