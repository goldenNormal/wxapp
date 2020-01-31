# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from bs4 import BeautifulSoup
from wxapp.items import WxappItem
class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp_spider'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'mod=list&catid=2&page=\d'), follow=True),
        Rule(LinkExtractor(allow=r'article-.+-.+\.html'), callback='parse_item', follow=False),
        )


    def parse_item(self, response):
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        soup=BeautifulSoup(response.text,'lxml')
        title=soup.select_one('#ct > div.mn > div > div.middle_info.cl > div > div.h.hm.cl > div:nth-child(1) > h1').text
        describe=soup.select_one('#ct > div.mn > div > div.middle_info.cl > div > div.blockquote > p').text
        print(title)
        print('='*50)
        # print(describe)
        # print('='*50)
        yield WxappItem(title=title,describe=describe)
        # print(title)
        # return item
