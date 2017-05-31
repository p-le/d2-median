# -*- coding: utf-8 -*-
import scrapy

class RuneItem(scrapy.Item):
    name = scrapy.Field()
    level = scrapy.Field()
    runes = scrapy.Field()
    rwType = scrapy.Field()
    description = scrapy.Field()
