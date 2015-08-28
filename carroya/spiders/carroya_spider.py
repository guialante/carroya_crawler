# -*- coding: utf-8 -*-
import scrapy

from ..items import CarroyaItem


class CarroyaSpider(scrapy.Spider):
    name = "crrya"
    allowed_domains = ["carroya.com"]
    start_urls = [
        "http://www.carroya.com/web/buscar/vehiculos/t4.do"
    ]

    def parse(self, response):

        for sel in response.xpath('//ul/li'):
            item = CarroyaItem()
            dt = sel.xpath('dl//a//dt')
            item['brand'] = dt.xpath('h2//em//text()').extract()
            item['price'] = dt.xpath('span//text()').extract()
            yield item
