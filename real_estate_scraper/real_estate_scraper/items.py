import scrapy

class RealEstateItem(scrapy.Item):
    location = scrapy.Field()
    nature = scrapy.Field()
    property_type = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()
    publication_date = scrapy.Field()
    area = scrapy.Field()
    description = scrapy.Field()
    contact = scrapy.Field()