class ContactItem(scrapy.Item):
    name = scrapy.Field()
    email = scrapy.Field()
    phone = scrapy.Field()
    address = scrapy.Field()