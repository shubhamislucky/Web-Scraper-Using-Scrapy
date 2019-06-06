#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 00:38:51 2019

@author: shubhamislucky
"""

import scrapy
from MyScraper.items import MovieItem

class ThirdSpider(scrapy.Spider):
    name = "ThirdSpider"
    allowed_domains = ["imdb.com"]
    start_urls = [
            "https://www.imdb.com/chart/top",
    
        ]
    def parse(self, response):
             links = response.xpath('//tbody[@class="lister-list"]/tr/td[@class="titleColumn"]/a/@href').extract()
             i = 1
             
             for link in links:
                 abs_url = response.urljoin(link)
                 url_next = '//*[@id="main"]/div/span/div/div/div[2]/table/tbody/tr['+str(i)+']/td[3]/strong/text()'
                 rating = response.xpath(url_next).extract()
                 if(i <= len(links)):
                     i = i+1
                     yield scrapy.Request(abs_url, callback = self.parse_indetail, meta={'rating' : rating})
                     
    def parse_indetail(self, response):
        item = MovieItem()
        item['title'] = response.xpath('//div[@class="title_wrapper"]/h1/text()').extract()[0][:-1]
        item['popularity'] = response.xpath('//div[@class="titleReviewBarSubItem"]/div/span/text()').extract()[2][21:-8]
        
        return item