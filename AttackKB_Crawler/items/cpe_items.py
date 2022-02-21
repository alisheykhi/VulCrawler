import scrapy

class CPEItems(scrapy.Item):

    WFN = scrapy.Field()
    FS = scrapy.Field()
    URI = scrapy.Field()
    Dict = scrapy.Field()
    name = scrapy.Field()
    type = scrapy.Field()
    vendor = scrapy.Field()
    product = scrapy.Field()
    version = scrapy.Field()
    update = scrapy.Field()
    edition = scrapy.Field()
    language = scrapy.Field()
    targetSoftware = scrapy.Field()
    targetHardware = scrapy.Field()
    softwareEdition = scrapy.Field()
    other = scrapy.Field()
    callback = scrapy.Field()