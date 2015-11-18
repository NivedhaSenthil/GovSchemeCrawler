# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SchemeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    department = scrapy.Field()
    district = scrapy.Field()
    name = scrapy.Field()
    beneficiaries = scrapy.Field()
    how_to_avail = scrapy.Field()
    valid_from = scrapy.Field()
    valid_till = scrapy.Field()
    description = scrapy.Field()
    eligible_age =scrapy.Field()
    eligible_income = scrapy.Field()
    eligible_community = scrapy.Field()
    eligible_other_details = scrapy.Field()
    
