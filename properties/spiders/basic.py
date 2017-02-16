import scrapy
from properties.items import PropertiesItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join
import urllib.parse
import socket
import datetime


class BasicSpider(scrapy.Spider):
    name = "basic"
    allowed_domains = ["web"]
    start_urls = ['http://scrapybook.s3.amazonaws.com/properties/index_00000.html']

    def parse(self, response):
        l = ItemLoader(item=PropertiesItem(), response=response)
        l.add_xpath('title', '//*[@itemprop="name"]/text()', MapCompose(str.strip, str.title))
        l.add_xpath('price', './/*[@itemprop="price"][1]/text()', MapCompose(lambda i: i.replace(',', ''), float), re='[,.0-9]+')
        l.add_xpath('description', '//*[@itemprop="description"]/text()', MapCompose(str.strip), Join())
        l.add_xpath('address', '//*[@itemtype="http://schema.org/Place"]/span/text()', MapCompose(str.strip))
        l.add_xpath('image_urls', '//*[@itemprop="image"]/@src', MapCompose(lambda i: urllib.parse.urljoin(response.url, i)))

        # Housekeeping fields
        l.add_value('url', response.url)
        l.add_value('project', self.settings.get('BOT_NAME'))
        l.add_value('spider', self.name)
        l.add_value('server', socket.gethostname())
        l.add_value('date', datetime.datetime.now())
        return l.load_item()