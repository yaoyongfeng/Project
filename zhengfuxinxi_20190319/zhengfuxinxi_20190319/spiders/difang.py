# -*- coding: utf-8 -*-
import scrapy


class DifangSpider(scrapy.Spider):
    name = 'difang'
    allowed_domains = ['stdaily.com']
    start_urls = ['http://www.stdaily.com/index/yaowen/yaowen.shtml']

    def parse(self, response):
        news_list = response.xpath("//div[@class='f_lieb_list']/dl")
        for new in news_list:
            new_title = new.xpath("./h3/a/text()").extract()[0]
            new_href = "http://www.stdaily.com" + new.xpath("./h3/a/@href").extract()[0]
            new_time = new.xpath("./dd/div[@class='dete']/span[@class='sp_1']/text()").extract()[0].strip()
            new_info = ','.join(new.xpath("./dd/div[@class='wenzi_box']/p/text()").extract()).strip()
            yield scrapy.Request(url=new_href,
                                 meta={'new_title': new_title, 'new_time': new_time, 'new_info': new_info},
                                 callback=self.parse_content)

    def parse_content(self, response):
        item = NewItem()
        new_from = response.xpath("//span[@class='f_source']/text()").extract()
        if len(new_from) == 0:
            item['new_from'] = '暂无来源'
        else:
            item['new_from'] = response.xpath("//span[@class='f_source']/text()").extract()[0]
        new_author = response.xpath("//span[@class='f_author']/text()").extract()
        if len(new_author) == 0:
            item['new_author'] = "暂无作者"
        else:
            item['new_author'] = response.xpath("//span[@class='f_author']/text()").extract()[0].strip()
        item['new_type'] = '>'.join(response.xpath(
            "/html/body/div[@class='container ']/div[@class='article f_zwnr']/ol[@class='breadcrumb']/a/text()").extract()) + '>正文'
        item['new_title'] = response.meta['new_title']
        item['new_time'] = response.meta['new_time'].replace('-', '/')
        item['new_info'] = response.meta['new_info']
        print(item)
        yield item
