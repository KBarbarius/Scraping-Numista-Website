# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CoinscraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass



class CoinItem(scrapy.Item):
    url = scrapy.Field()
    coin_name = scrapy.Field()
    field1 = scrapy.Field()
    field2 = scrapy.Field()
    field3 = scrapy.Field()
    field4 = scrapy.Field()
    field5 = scrapy.Field()
    field6 = scrapy.Field()
    field7 = scrapy.Field()
    field8 = scrapy.Field()
    field9 = scrapy.Field()
    field10 = scrapy.Field()
    field11 = scrapy.Field()
    field12 = scrapy.Field()
    field13 = scrapy.Field()
    field14 = scrapy.Field()
    field15 = scrapy.Field()
    observe_description =  scrapy.Field()
    reverse_description =  scrapy.Field()
    mintage =  scrapy.Field()
    observe_img =  scrapy.Field()
    reverse_img =  scrapy.Field()

