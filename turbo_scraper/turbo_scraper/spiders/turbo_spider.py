import scrapy
from turbo_scraper.items import TurboScraperItem
from scrapy.loader import ItemLoader

class TurboSpiderSpider(scrapy.Spider):
    name = "turbo_spider"
    allowed_domains = ["turbo.az"]
    url = "https://turbo.az/autos?q%5Bsort%5D=&q%5Bmake%5D%5B%5D=8&q%5Bmodel%5D%5B%5D=&q%5Bmodel%5D%5B%5D=526&q%5Bused%5D=&q%5Bregion%5D%5B%5D=&q%5Bprice_from%5D=&q%5Bprice_to%5D=&q%5Bcurrency%5D=azn&q%5Bloan%5D=0&q%5Bbarter%5D=0&q%5Bcategory%5D%5B%5D=&q%5Byear_from%5D=2017&q%5Byear_to%5D=&q%5Bcolor%5D%5B%5D=&q%5Bfuel_type%5D%5B%5D=&q%5Bgear%5D%5B%5D=&q%5Btransmission%5D%5B%5D=&q%5Bengine_volume_from%5D=&q%5Bengine_volume_to%5D=&q%5Bpower_from%5D=&q%5Bpower_to%5D=&q%5Bmileage_from%5D=&q%5Bmileage_to%5D=&q%5Bonly_shops%5D=&q%5Bprior_owners_count%5D%5B%5D=&q%5Bseats_count%5D%5B%5D=&q%5Bmarket%5D%5B%5D=&q%5Bcrashed%5D=1&q%5Bpainted%5D=1&q%5Bfor_spare_parts%5D=0"

    def start_requests(self):
        yield scrapy.Request(url=self.url,callback=self.parse)
    
    def parse(self,response):
        next_page = response.xpath('//a[@rel="next"]/@href').get()
        
        for car_url in response.xpath('//a[@class="products-i__link"]/@href').getall():
            yield scrapy.Request(url='https://turbo.az'+car_url,callback=self.parse_item)
        
        if next_page is not None:
            yield scrapy.Request('https://turbo.az'+next_page,callback=self.parse)

    def parse_item(self, response):
        car_item = ItemLoader(item=TurboScraperItem(),response=response)
        car_item.add_xpath('title','//h1[@class="product-title"]/text()')
        car_item.add_xpath('price','//div[@class="product-price__i product-price__i--bold"]/text()')
        car_item.add_value('link',response.url)
        car_item.add_xpath('make','//label[@for="ad_make_id"]/following-sibling::span/a/text()')
        car_item.add_xpath('model','//label[@for="ad_model"]/following-sibling::span/a/text()')
        car_item.add_xpath('year','//label[@for="ad_reg_year"]/following-sibling::span/a/text()')
        car_item.add_xpath('odometer','//label[@for="ad_mileage"]/following-sibling::span/text()')
        car_item.add_xpath('color','//label[@for="ad_color"]/following-sibling::span/text()')
        car_item.add_value('engine_displacement',response.xpath('//label[@for="ad_engine_volume"]/following-sibling::span/text()').get().split('/')[0])
        car_item.add_value('horsepower',response.xpath('//label[@for="ad_engine_volume"]/following-sibling::span/text()').get().split('/')[1])
        car_item.add_value('fuel_type',response.xpath('//label[@for="ad_engine_volume"]/following-sibling::span/text()').get().split('/')[2])
        car_item.add_xpath('transmission','//label[@for="ad_transmission"]/following-sibling::span/text()')
        car_item.add_xpath('drive_train','//label[@for="ad_gear"]/following-sibling::span/text()')
        car_item.add_xpath('body_style','//label[@for="ad_category"]/following-sibling::span/text()')
        car_item.add_xpath('location','//label[@for="ad_region"]/following-sibling::span/text()')
        car_item.add_xpath('owner','//div[@class="product-owner__info-name"]/text()')
        car_item.add_xpath('phone','//a[@class="product-phones__list-i"]/text()')

        yield car_item.load_item()