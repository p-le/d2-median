# -*- coding: utf-8 -*-
import scrapy
from rune.items import RuneItem

class MedianxlSpider(scrapy.Spider):
    name = "medianxl"
    allowed_domains = ["docs.median-xl.com"]
    start_urls = ['https://docs.median-xl.com/doc/items/runewords']

    def parse(self, response):
        trs = response.xpath('//table/tbody/tr')
        data = list()
        for tr in trs:
            tds = tr.xpath('td')
            rw = RuneItem()
            if len(tds) == 1:
                continue
            parts = tds[0].xpath('span//text()').extract()
            if len(parts) == 2:
                (name, level) = parts
                rw['name'] = name.strip()
                rw['level'] = int(level.strip().replace("Level ", ""))
            if len(parts) == 3:
                (name, postfix, level) = parts
                rw['name'] = name.strip() + " " + postfix.strip()
                rw['level'] = int(level.strip().replace("Level ", ""))
            if len(parts) == 4:
                (name, postfix1, postfix2, level) = parts
                rw['name'] = name.strip() + " " + postfix1.strip() + " " + postfix2.strip()
                rw['level'] = int(level.strip().replace("Level ", ""))
            parts = tds[3].xpath('text()').extract()
            rw['rwType'] = parts[0].strip()
            parts = tds[4].xpath('span/text()').extract()
            rw['description'] = parts
            parts = tds[2].xpath('b//text()').extract()
            aPart = [s.strip() for s in parts if s.strip()]
            rw['runes'] = aPart
            yield rw
