import scrapy
from ..items import *
import json,time,datetime,re


class ZhengqunaSpider(scrapy.Spider):
    name = 'zhengquna'
    def start_requests(self):
        for page in range(1,2):
            headers = {
                "Referer": "http://www.cnstock.com/",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
            }
            yield scrapy.Request(url='http://app.cnstock.com/api/waterfall?callback=&colunm=sd&page=+str(page)+',callback=self.parse,headers=headers)
    def parse(self, response):
        js = json.loads(response.text.strip())
        data = js['data']['item']
        for a in data:
            headers = {
                "Referer": "http://www.cnstock.com/",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
            }

            # 1.拿到列表页的 内容拿到这个列表页文章的标题
            title = a['title']
            # 列表页的 这个ID
            caijing_id = a['id']
            # 3.拿到列表页时间 替换一下时间的格式
            shi = a['dateline']
            fb_time = shi.replace('年','-').replace('月','-').replace('日','')

            # 15. 配图url
            peitu_url = a['i']

            item = CaijingItem()
            item['title'] = time
            item['caijing_id'] = caijing_id
            item['fb_time'] = fb_time
            item['peitu_url'] = peitu_url


            # 8. 详情页链接
            deatil_url = a['link']
            yield scrapy.Request(url=deatil_url,callback=self.detail,headers=headers,meta={'item':item})
    def detail(self,response):
        item = response.meta['item']
        all_div = response.xpath("//div[@id='pager-content']")

        for div in all_div:
            # 4. 作者
            author = div.xpath("./div[@class='bullet'][1]/span[@class='author']/text()").extract()[0]
            # 5. 阅读量
            try:
                yd_liang = ''
            except Exception:
                yd_liang = ''
            # 6. 导读
            try:
                daodu = ''
            except Exception:
                daodu = ''
            # 7. 内容
            content = ''.join(div.xpath("./div[@id='qmt_content_div']/p/text()").extract())

            # 9. 关键字
            try:
                guanjianzi = ''
            except Exception:
                guanjianzi = ''
            # 10. 免责声明
            try:
                mz_shengming = ''
            except Exception:
                mz_shengming = ''
            # 11. 爬取时间
            now = time.time()
            pq_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            # 2. 文章的来源
            try:
                laiyuan = div.xpath(".//div[@class='bullet'][1]/span[@class='source']/a/text()").extract()[0]
            except Exception:
                laiyuan = ''
            # 12. 阅读数
            try:
                yd_shu = ''
            except Exception:
                yd_shu = ''
            # 13. 粉丝数
            try:
                fs_shu = ''
            except Exception:
                fs_shu = ''
            # 14. 评论数
            try:
                pl_shu = ''
            except Exception:
                pl_shu = ''

            # 16.刊登报刊
            try:
                kd_baokan = ''
            except Exception:
                kd_baokan = ''
            # 17. 当前位置
            try:
                weizhi = ''
            except Exception:
                weizhi = ''

            item['author'] = author
            item['yd_liang'] = yd_liang
            item['daodu'] = daodu
            item['content'] = content
            item['guanjianzi'] = guanjianzi
            item['mz_shengming'] = mz_shengming
            item['pq_time'] = pq_time
            item['laiyuan'] = laiyuan
            item['yd_shu'] = yd_shu
            item['fs_shu'] = fs_shu
            item['pl_shu'] = pl_shu
            item['kd_baokan'] = kd_baokan
            item['weizhi'] = weizhi
            yield item





