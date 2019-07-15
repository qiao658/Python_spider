# -*- coding: utf-8 -*-
import scrapy
import re
from movie_spider.items import MovieItem


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['80s.la']
    start_urls = ['https://www.80s.la/movie/list']

    def parse(self, response):
        url = response.xpath("//ul[contains(@class,'me1')]//li/a/@href").getall()
        movie_urls = list(map(lambda x: "https://www.80s.la" + x, url))
        for movie_url in movie_urls:
            yield scrapy.Request(movie_url, callback=self.parse_detail)

    def parse_detail(self, response):
        # 标题
        title = response.xpath("//div[@class='info']//h1/text()").get()
        title = re.sub(r"\s", "", title)
        # 剧情介绍
        info = re.findall(
            r'<p style="display:none;" id="movie_content_all"><span class="font_888">(.*?)</p>',
            response.text, flags=re.DOTALL)[0]
        info = re.sub("</span>", "", info)
        # 图片url https://img.akqipai.com/upload/img/1906/0812801001561721401.jpg
        img_url = response.xpath("//div[@class='img']/img/@src").getall()
        img_url = list(map(lambda x: "https:" + x, img_url))[0]
        # 本地下载链接
        link = response.xpath("//span[contains(@class,'dlbutton3')]/a/@href").get()
        # print(title, info, img_url, link)

        yield MovieItem(mname=title, mdesc=info, mimg=img_url, mlink=link)
