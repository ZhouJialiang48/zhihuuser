# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class UserItem(scrapy.Item):
    user_type = Field()
    answer_count = Field()
    url_token = Field()
    uid = Field()
    articles_count = Field()
    name = Field()
    headline = Field()
    gender = Field()
    follower_count = Field()
