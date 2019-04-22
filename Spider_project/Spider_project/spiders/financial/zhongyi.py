import scrapy,datetime
from ..items import ZhongyicaijingItem


class ZhongyiSpider(scrapy.Spider):
    name = 'zhongyi'
    # allowed_domains = ['aaa']
    start_urls = ['http://www.zhongyi9999.com/zqsc/ssgs/']

    def parse(self, response):
        xinwen_list_url = response.xpath("//div[@class='list-p-l-nav-c']/a/@href").extract()
        for list_url in xinwen_list_url:
            li_url = 'http://www.zhongyi9999.com'+list_url
            for page in range(1,103):
                url = li_url+'/index_'+str(page)+'.html'
                yield scrapy.Request(url=url,callback=self.liebiaoye)

    def liebiaoye(self,response):
        # 列表页的查找
        list_div = response.xpath("//li[@class='list-p-main-i']")

        for div in list_div:
            # 拿到列表页的配图的 url
            peitu_url = div.xpath("./a[@class='list-p-m-img']/img/@src").extract()[0]
            # 5. 阅读量
            yd_liang = div.xpath(".//span[@class='fr fc808']/text()").extract()[0]

            # 拿到列表页的标题的 url 进入详情页进行爬取里面内容
            try:
                detail_url = 'http://www.zhongyi9999.com'+div.xpath("./div[@class='list-p-m-info fr']/a/@href").extract()[0]
            except Exception:
                detail_url = '这篇文章不存在！'

            item = ZhongyicaijingItem()
            item['peitu_url'] = peitu_url
            item['yd_liang'] = yd_liang
            item['detail_url'] = detail_url

            yield scrapy.Request(url=detail_url,callback=self.detail,meta={'item':item})

    def detail(self,response):
        item = response.meta['item']
        da_div = response.xpath("//div[@class='page-left']")
        for da in da_div:
            # 1. 标题
            title = da.xpath("./h1[@class='c-title f28']/text()").extract()[0]
            # 2. 来源
            laiyuan = da.xpath(".//span[@class='fr']/text()").extract()[0]
            # 3. 发布时间
            fb_time = da.xpath(".//span[@class='mtr34'][2]/text()").extract()[0]
            # 4. 作者
            author = da.xpath(".//span[@class='mtr34'][1]/a[@id='author']/text()").extract()[0]
            # 6. 导读
            daodu = da.xpath("./div[@class='fc808 f14 c-intro']/text()").extract()[0].strip()
            # 7. 内容
            content = ''.join(da.xpath("./div[@class='c-con']/p/text()").extract()[0].strip())
            # 9. 关键字
            guanjianzi = da.xpath("./div[@class='c-keys']/a/text()").extract()[0]
            # 10. 免责声明
            mz_shengming = da.xpath(".//span[@class='fc808'][1]/text()").extract()[0]
            # 11. 爬取时间
            pq_time = datetime.datetime.now()
            # 12. 阅读数
            try:
                yd_shu = scrapy.Field()
            except Exception:
                yd_shu = ''
            # 13. 粉丝数
            try:
                fs_shu = scrapy.Field()
            except Exception:
                fs_shu = ''
            # 14. 评论数
            try:
                pl_shu = scrapy.Field()
            except Exception:
                pl_shu = ''

            # 16.刊登报刊
            try:
                kd_baokan = scrapy.Field()
            except Exception:
                kd_baokan = ''

            # 17. 当前位置
            weizhi = ' '.join(da.xpath("./div[@class='c-h f14']/a/text()").extract())

            # id 的爬取
            try:
                caijing_id = scrapy.Field()
            except Exception:
                caijing_id = ''

            item['title'] = title
            item['laiyuan'] = laiyuan
            item['fb_time'] = fb_time
            item['author'] = author
            item['daodu'] = daodu
            item['content'] = content
            item['guanjianzi'] = guanjianzi
            item['mz_shengming'] = mz_shengming
            item['pq_time'] = pq_time
            item['yd_shu'] = yd_shu
            item['fs_shu'] = fs_shu
            item['pl_shu'] = pl_shu
            item['kd_baokan'] = kd_baokan
            item['weizhi'] = weizhi
            item['caijing_id'] = caijing_id






