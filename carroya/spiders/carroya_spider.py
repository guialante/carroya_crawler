# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

from ..items import CarroyaItem


class CarroyaSpider(scrapy.Spider):
    
    name = "carroya"
    allowed_domains = ["carroya.com"]
    
    start_urls = [
        'http://www.carroya.com/web/buscar/vehiculos/t4.do'
    ]

    def parse(self, response):
        links = response.xpath('//a[@class="detalleOrden3"]/@href').extract()
        
        for link in links:
            url = response.urljoin(link)
            yield Request(url, callback=self.parse_item, dont_filter=True)

        next_page_url = response.xpath(
            '//ul[@class="pagination"]//a[contains(text(), "»")]/@href'
        ).extract_first(default='')

        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield Request(next_page_url, callback=self.parse, dont_filter=True)

    def parse_item(self, response):
        item = CarroyaItem()

        item['brand'] = response.xpath('//main[@id="detailUsed"]//input[@id="marca"]/@value').extract_first(default='')
        item['price'] = response.xpath('//main[@id="detailUsed"]//input[@id="precio"]/@value').extract_first(default='')
        item['year'] = response.xpath('//main[@id="detailUsed"]//input[@id="modelo"]/@value').extract_first(default='')
        item['status'] = response.xpath(
            '//main[@id="detailUsed"]//input[@id="estadoDetalle"]/@value'
        ).extract_first(default='')
        item['trim'] = response.xpath('//main[@id="detailUsed"]//input[@id="linea"]/@value').extract_first(default='')
        item['url'] = response.request.url
        item['kilometers'] = response.xpath(
            '//main[@id="detailUsed"]//input[@id="kilometraje"]/@value'
        ).extract_first(default='')
        item['city'] = response.xpath('//main[@id="detailUsed"]//input[@id="ciudad"]/@value').extract_first(default='')
        item['type'] = response.xpath(
            '//main[@id="detailUsed"]//input[@id="s_prop40"]/@value'
        ).extract_first(default='')
        yield item

