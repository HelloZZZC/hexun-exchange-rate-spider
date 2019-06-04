# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
from hexun.util.db import DBConnection


class HexunPipeline(object):
    def process_item(self, item, spider):
        sql = "INSERT INTO `exchange_rate` ( `from_currency`, `to_currency`, `rate`, `created_time`, `updated_time`) VALUES (%s, %s, %s, %s, %s)"
        params = (item['from_currency'], item['to_currency'], item['rate'], int(time.time()), int(time.time()))
        conn = DBConnection()
        conn.execute(sql, params)
        return item
