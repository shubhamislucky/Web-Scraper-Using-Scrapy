#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:12:38 2019

@author: shubhamislucky
"""

import scrapy

class SongScraper(scrapy.Spider):
    name = "SongScraper"
    allowed_domains = ['www.gaana.com']
    start_urls = ['https://gaana.com/playlist/gaana-dj-gaana-international-top-50']
    
    def parse(self, response):
        titles = response.xpath('//a[contains(@data-type, "playSong")]/text()').extract()
        artists = response.xpath('//a[contains(@data-type, "url")]/text()').extract()        
        for (title, artist) in zip(titles, artists):
            scraped_info = {
                    'title' : title,
                    'artists' : artist
                    }
        
            yield scraped_info