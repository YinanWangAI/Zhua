# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TechcrunchPipeline(object):
    def __init__(self):
        self.f = open("item.csv", "w", encoding="utf-8")

    def process_item(self, item, spider):
        item = dict(item)
        line = item["date"] + ',"' + item["title"] + '",' + \
               item["url"] + '\n'
        self.f.write(line)
