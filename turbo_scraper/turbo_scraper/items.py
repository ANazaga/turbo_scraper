# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
# from scrapy.loader import ItemLoader

class TurboScraperItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()