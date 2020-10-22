# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TbsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    parent_node = scrapy.Field
    child_node = scrapy.Field
