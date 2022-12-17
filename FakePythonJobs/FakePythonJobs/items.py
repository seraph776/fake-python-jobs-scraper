# Define here the models for your scraped items

import scrapy
from scrapy.loader import Item, ItemLoader
from itemloaders.processors import TakeFirst, MapCompose

class FakePythonjobsItem(Item):
    # define the fields for your item here like:
    job_name = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    date_posted = scrapy.Field()
    apply_link = scrapy.Field()


class FakePythonjobsItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    job_name_in = MapCompose(str.strip)
    company_in = MapCompose(str.strip)
    location_in = MapCompose(str.strip)
    date_posted_in = MapCompose(str.strip)
    apply_link_in = MapCompose(str.strip)