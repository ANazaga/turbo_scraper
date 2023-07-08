import scrapy


class TurboSpiderSpider(scrapy.Spider):
    name = "turbo_spider"
    allowed_domains = ["turbo.az"]
    start_urls = ["https://turbo.az/"]

    def parse(self, response):
        pass
