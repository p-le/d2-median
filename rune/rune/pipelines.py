# -*- coding: utf-8 -*-
import json

class RunePipeline(object):
    def open_spider(self, spider):
        self.file = open('rw.json', 'w')
    def close_spider(self, spider):
        self.file.close()
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
