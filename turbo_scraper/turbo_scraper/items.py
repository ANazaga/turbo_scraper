import scrapy
from scrapy import Item, Field

class TurboScraperItem(Item):
    location = Field()
    make = Field()
    model = Field()
    year = Field()
    color = Field()
    engine_displacement = Field()
    horsepower = Field()
    fuel_type = Field()
    odometer = Field()
    transmission = Field()
    drive_train = Field()
    body_style = Field()
    title = Field()
    price = Field()
    owner = Field()
    phone = Field()
    link = Field()