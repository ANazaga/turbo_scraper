import scrapy
from turbo_scraper.items import TurboScraperItem
from scrapy.loader import ItemLoader

class TurboSpiderSpider(scrapy.Spider):
    name = "turbo_spider"
    allowed_domains = ["turbo.az"]
    start_urls = ["https://turbo.az/autos?q%5Bsort%5D=&q%5Bmake%5D%5B%5D=3&q%5Bmodel%5D%5B%5D=&q%5Bused%5D=&q%5Bregion%5D%5B%5D=&q%5Bprice_from%5D=&q%5Bprice_to%5D=&q%5Bcurrency%5D=azn&q%5Bloan%5D=0&q%5Bbarter%5D=0&q%5Bcategory%5D%5B%5D=&q%5Byear_from%5D=&q%5Byear_to%5D=&q%5Bcolor%5D%5B%5D=&q%5Bfuel_type%5D%5B%5D=&q%5Bgear%5D%5B%5D=&q%5Btransmission%5D%5B%5D=&q%5Bengine_volume_from%5D=&q%5Bengine_volume_to%5D=&q%5Bpower_from%5D=&q%5Bpower_to%5D=&q%5Bmileage_from%5D=&q%5Bmileage_to%5D=&q%5Bonly_shops%5D=&q%5Bprior_owners_count%5D%5B%5D=&q%5Bseats_count%5D%5B%5D=&q%5Bmarket%5D%5B%5D=&q%5Bcrashed%5D=1&q%5Bpainted%5D=1&q%5Bfor_spare_parts%5D=0"]

    def parse(self, response):
        for car in response.xpath('//div[@class="products-i__bottom"]'):
            car_item = ItemLoader(item=TurboScraperItem(),selector=car)
            car_item.add_xpath('title','.//div[@class="products-i__name products-i__bottom-text"]/text()')
            car_item.add_xpath('price','.//div[@class="product-price"]/text()')
            yield car_item.load_item()

        next_page = response.xpath('//a[@rel="next"]/@href').get()
        if next_page is not None:
            yield scrapy.Request('https://turbo.az'+next_page,callback=self.parse)