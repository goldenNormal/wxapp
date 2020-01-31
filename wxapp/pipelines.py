# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class WxappPipeline(object):
    def __init__(self):
        self.fp=open('3.json','w',encoding='utf-8')

    def open_spider(self,spider):
        print("开始")
    def process_item(self, item, spider):
        print("到这了")
        print(item)
        self.fp.write(json.dumps(dict(item),ensure_ascii=False)+'\n')

        return item
    def close_spider(self,spider):
        self.fp.close()