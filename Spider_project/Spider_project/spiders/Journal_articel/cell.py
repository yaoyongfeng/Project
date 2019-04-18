# -*- coding: utf-8 -*-
from googletrans import Translator
import scrapy

class CellSpider(scrapy.Spider):
    name = 'cell'
    # allowed_domains = []
    start_urls = ['https://www.cell.com/']

    def parse(self, response):
            pass
