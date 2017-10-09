# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CarroyaItem(scrapy.Item):
    brand = scrapy.Field()
    price = scrapy.Field()
    year = scrapy.Field()
    status = scrapy.Field()
    trim = scrapy.Field()
    url = scrapy.Field()
    kilometers = scrapy.Field()
    city = scrapy.Field()
    type = scrapy.Field()

