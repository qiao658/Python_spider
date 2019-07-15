# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors


# 普通的MySQL存储
class MovieSpiderPipeline(object):
    def __init__(self):
        dbparams = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',  # 一般是root用户吧
            'password': '你的MySQL密码',
            'database': "你的MySQL数据库名",
            "charset": 'utf8'
        }
        self.conn = pymysql.connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql = None

    def process_item(self, item, spider):
        self.cursor.execute(self.sql,
                            (item['mname'], item['mdesc'], item['mimg'], item['mlink']))
        self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
            insert into 表名(mid,mname,mdesc,mimg,mlink)values(null,%s,%s,%s,%s)
            """
            return self._sql
        return self._sql


# 异步的MySQL存储
class MovieTwistedPipeline(object):
    def __init__(self):
        dbparams = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': '123456',
            'database': "account",
            "charset": 'utf8',
            'cursorclass': cursors.DictCursor
        }
        self.dbpool = adbapi.ConnectionPool('pymysql', **dbparams)
        self._sql = None

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
                        insert into 表名(mid,mname,mdesc,mimg,mlink)values(null,%s,%s,%s,%s)
                        """
            return self._sql
        return self._sql

    def process_item(self, item, spider):
        defer = self.dbpool.runInteraction(self.insert_item, item)
        defer.addErrback(self.handle_error)

    def insert_item(self, cursor, item):
        cursor.execute(self.sql,
                       (item['mname'], item['mdesc'], item['mimg'], item['mlink']))

    def handle_error(self, error, item, spider):
        print('=' * 10 + "error" + '=' * 10)
        print(error)
        print('=' * 10 + "error" + '=' * 10)
