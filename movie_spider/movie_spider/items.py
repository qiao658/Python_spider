# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    mname = scrapy.Field()

    mdesc = scrapy.Field()

    mimg = scrapy.Field()

    mlink = scrapy.Field()
