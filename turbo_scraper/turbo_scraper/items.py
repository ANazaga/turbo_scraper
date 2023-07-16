import scrapy
from scrapy import Item, Field
from itemloaders.processors import TakeFirst, MapCompose

class TurboScraperItem(Item):
    location = Field(output_processor=TakeFirst())
    make = Field(output_processor=TakeFirst())
    model = Field(output_processor=TakeFirst())
    year = Field(output_processor=TakeFirst())
    color = Field(output_processor=TakeFirst())
    engine_displacement = Field(output_processor=TakeFirst())
    horsepower = Field(output_processor=TakeFirst())
    fuel_type = Field(output_processor=TakeFirst())
    odometer = Field(output_processor=TakeFirst())
    transmission = Field(output_processor=TakeFirst())
    drive_train = Field(output_processor=TakeFirst())
    body_style = Field(output_processor=TakeFirst())
    title = Field(input_processor=MapCompose(lambda x:x.strip().replace(',','')),output_processor=TakeFirst())
    price = Field(output_processor=TakeFirst())
    owner = Field(output_processor=TakeFirst())
    phone = Field()
    link = Field(output_processor=TakeFirst())