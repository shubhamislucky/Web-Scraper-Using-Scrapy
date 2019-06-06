#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 21:35:41 2019

@author: shubhamislucky
"""

import scrapy
from MyScraper.items import NewItem

class SecondScrapy(scrapy.Spider):
    name = "SecondSpider"
    allowed_domains = ['www.superdatascience.com']
    start_urls = [
            'https://superdatascience.com/artificial-intelligence',
            ]
    
    def parse(self, response):
        item = NewItem()
        item['main_headline'] = response.xpath('//span/text()').extract()
        item['headline'] = response.xpath('//title/text()').extract()
        item['url'] = response.url
        item['project'] = self.settings.get('BOT_NAME')
        item['spider'] = self.name
        
        
        