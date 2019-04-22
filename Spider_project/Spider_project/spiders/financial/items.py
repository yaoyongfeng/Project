# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CaijingItem(scrapy.Item):

    # 1. 标题
    title = scrapy.Field()
    # 2. 来源
    laiyuan = scrapy.Field()
    # 3. 发布时间
    fb_time = scrapy.Field()
    # 4. 作者
    author = scrapy.Field()
    # 5. 阅读量
    yd_liang = scrapy.Field()
    # 6. 导读
    daodu = scrapy.Field()
    # 7. 内容
    content = scrapy.Field()
    # 8. 详情页链接
    deatil_url = scrapy.Field()
    # 9. 关键字
    guanjianzi = scrapy.Field()
    # 10. 免责声明
    mz_shengming = scrapy.Field()
    # 11. 爬取时间
    pq_time = scrapy.Field()
    # 12. 粉丝数
    fs_shu = scrapy.Field()
    # 13. 评论数
    pl_shu = scrapy.Field()
    # 14. 配图url
    peitu_url = scrapy.Field()
    # 15. 刊登报刊
    kd_baokan = scrapy.Field()
    # 16. 当前位置
    weizhi = scrapy.Field()
    # 17. id信息
    caijing_id = scrapy.Field()



