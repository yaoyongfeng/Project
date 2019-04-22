# -*- coding: utf-8 -*-
import scrapy,json,re,datetime
from caijing.items import CaijingItem

from scrapy.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor

class JufengSpider(CrawlSpider):
    name = 'dongfangcaifu'
    start_urls = ['http://finance.eastmoney.com/a/ccjdd.html']
    rules = (
        Rule(LinkExtractor(allow=r"http://finance.eastmoney.com/a/ccjdd_\d+.html"),follow=True),
        Rule(LinkExtractor(allow=r"http://\w+.\w+.com/a/\d+.html"),callback='parse_item'),

        )
    site_name = "东方财富网"
    def parse_item(self, response):

        item = CaijingItem()
        sel = Selector(response)
        # 1. 标题
        title = sel.xpath("//div[@class='newsContent']/h1/text()").extract()
        if len(title):
            title = title[0]
        else:
            title = 'ok'
        # 2. 来源
        laiyuan = sel.xpath("string(//div[@class='source data-source'])").re("来源：\r\n(.*?)$")
        if len(laiyuan):
            laiyuan = laiyuan[0].strip()
        else:
            laiyuan = self.site_name
        # 3. 发布时间
        fb_time = sel.xpath("//div[@class='time']/text()").extract()
        if len(fb_time):
            fb_time = fb_time[0].replace("年","-").replace("月","-").replace("日","")
        # 4. 作者
        author = sel.xpath("//div[@class='author']/text()").re("作者：(.*?)$")
        if len(author):
            author = author[0]
        else:
            author = '匿名用户'
        # 5. 阅读量
        yd_liang = sel.xpath("string(//div[@id='comBodyEnd']/a[1])").re("共(.*?)人参与讨论")
        if len(yd_liang):
            yd_liang = yd_liang[0]
        else:
            yd_liang = '0'
        # 6. 导读
        daodu = sel.xpath("string(//div[@id='ContentBody']/div[@class='b-review'])").extract()
        if len(daodu):
            daodu = daodu[0]
        # 7. 内容
        content = sel.xpath("string(//div[@id='ContentBody']/p)").extract()
        if len(content):
            content = content[0]
        # 8. 详情页链接
        deatil_url = response.url
        # 9. 关键字
        guanjianzi = sel.xpath("//div[@id='ContentBody']//a[@class='infokey ']/text()").extract()
        guanjianzi = '、'.join(guanjianzi)
        # 10. 免责声明
        mz_shengming = ''
        # 11. 爬取时间
        pq_time = datetime.datetime.now()
        # 12. 粉丝数
        fs_shu = ''
        # 13. 评论数
        pl_shu = sel.xpath("string(//div[@id='comBodyEnd']/a[1])").re("已有(.*?)人评论")
        if len(pl_shu):
            pl_shu = pl_shu[0]
        else:
            pl_shu = 0
        # 14. 配图url
        peitu_url = ''
        # 15. 刊登报刊
        kd_baokan = sel.xpath("//div[@id='ContentBody']/p[@class='em_media']/text()").re("文章来源：(.*?)）")
        if len(kd_baokan):
            kd_baokan = kd_baokan[0]
        else:
            kd_baokan = self.site_name
        # 16. 当前位置
        weizhi = sel.xpath("string(//div[@id='Column_Navigation'])").extract()[0].strip()
        if '\r\n' in weizhi:
            weizhi = weizhi.split('\r\n')
        weizhi1 = ''
        for wei in weizhi:
            wei = wei.strip()
            weizhi1 += wei
        weizhi = weizhi1.replace('>','')
        # 17. id信息
        caijing_id = ''
        item["title"] = title
        item["yd_liang"] = yd_liang
        item["daodu"] = daodu
        item["deatil_url"] = deatil_url
        item["guanjianzi"] = guanjianzi
        item["mz_shengming"] = mz_shengming
        item["pq_time"] = pq_time
        item["fs_shu"] = fs_shu
        item["pl_shu"] = pl_shu
        item["peitu_url"] = peitu_url
        item["weizhi"] = weizhi
        item["caijing_id"] = caijing_id
        item["laiyuan"] = laiyuan
        item["author"] = fb_time
        item["yd_liang"] = author
        item["content"] = content
        item["kd_baokan"] = kd_baokan
        yield item
