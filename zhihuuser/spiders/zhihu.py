# -*- coding: utf-8 -*-
import json
import scrapy
from zhihuuser.items import UserItem


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    BASE_URL = 'https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={offset}&limit={limit}'
    LIMIT = 20
    offset = 0
    start_urls = [BASE_URL.format(limit=LIMIT, offset=offset)]

    def parse(self, response):
        items = json.loads(response.body, encoding='utf8')['data']
        print(len(items))
        for item in items:
            user = UserItem()
            user['user_type'] = item['user_type']
            user['answer_count'] = item['answer_count']
            user['url_token'] = item['url_token']
            user['uid'] = item['id']
            user['articles_count'] = item['articles_count']
            user['name'] = item['name']
            user['headline'] = item['headline']
            user['gender'] = item['gender']
            user['follower_count'] = item['follower_count']
            yield user
        if not json.loads(response.body, encoding='utf8')['paging']['is_end']:
            self.offset += 20
            next_url = self.BASE_URL.format(limit=self.LIMIT, offset=self.offset)
            yield scrapy.Request(url=next_url, callback=self.parse)
