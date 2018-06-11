# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import json
import codecs
    
class MyprojectPipeline(object):
    def __init__(self):
        
        self.file = codecs.open('data.json', 'w', encoding='utf-8')
    
    def process_item(self, item, spider):
        
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        #line = json.dumps(sorted(item['title'],item['desc']), ensure_ascii=False) + "\n"
        self.file.write(line)
        
        return item
   
    def open_spider(self, spider):
        pass
   
    def close_spider(self, spider):
        pass
