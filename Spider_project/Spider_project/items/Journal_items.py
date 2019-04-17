# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class JournalItem(scrapy.item):
        # 期刊信息
        journal_meta = scrapy.Field()
        # 期刊唯一值
        identifier = scrapy.Field()
        # 论文标题
        title = scrapy.Field()
        # 标题翻译
        title_alternative = scrapy.Field()
        # 作者信息
        contributer_list = scrapy.Field()
        # 所属学科信息
        subject_list = scrapy.Field()
        # 摘要
        abstract = scrapy.Field()
        # 自定义摘要
        custom_abstract = scrapy.Field()
        # 摘要翻译
        abstract_alternative = scrapy.Field()
        # 期刊名
        journal_title = scrapy.Field()
        # 文章发布时间
        pubulication_date = scrapy.Field()
        # 文章发布年份
        pubulication_year = scrapy.Field()
        # 期刊卷
        volume = scrapy.Field()
        # 期
        issue = scrapy.Field()
        # 期刊地址链接
        journal_url = scrapy.Field()
        # 文章参考信息
        reference_list = scrapy.Field()
        # 文章地址
        detail_url = scrapy.Field()
        # 附件信息
        file_list = scrapy.Field()
        # 域名
        domain = scrapy.Field()
        # 文章所在期号地址
        volume_link = scrapy.Field()
        # 关键词
        keywords = scrapy.Field()
        # 自定义关键词
        custom_keywords = scrapy.Field()
        # 关键词翻译
        keywords_alternative = scrapy.Field()
        # 期刊备案信息地址
        identifier_url = scrapy.Field()
        # 语言
        language = scrapy.Field()
        # 访问权限
        access = scrapy.Field()
        # 正文html
        html_content = scrapy.Field()
        # 数据唯一id
        hash_code = scrapy.Field()
        # 文章所在模块
        module = scrapy.Field()
        # 正文
        content = scrapy.Field()
        # 自定义关键词翻译
        custom_keywords_alternative = scrapy.Field()
        # 自定义摘要翻译
        custom_abstract_alternative = scrapy.Field()
        # 文章所在期刊的起始页
        page_start = scrapy.Field()
        # 文章所在期刊的结束页
        page_end = scrapy.Field()
        # 扩展字段
        extension_meta = scrapy.Field()
        # 爬取时间
        create_date = scrapy.Field()
        # PDF链接
        file_url = scrapy.Field()
        # 更新到oss上的链接
        oss_url = scrapy.Field()

