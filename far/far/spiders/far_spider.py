import scrapy
import json
import re
from far.far.items import FarItem


class Captcha(scrapy.Spider):
    name = 'Captcha'
    allowed_domains = ['www.farpost.ru']
    start_urls = ['http://www.farpost.ru/']


    def __init__(self, headers, cookies):
        super(Captcha, self).__init__()
        self.headers = headers
        self.cookies = cookies

    def start_requests(self):
        yield scrapy.Request(
                    url='https://www.farpost.ru/vladivostok/service/internet',
                    cookies=self.cookies,
                    headers=self.headers,
                    callback=self.parse,
            )


    # Метод сбора основных данных
    def parse(self, response):
        item = FarItem()

        if response.css('title::text').extract()[0] == 'Фарпост - доска объявлений':
            item['is_captcha'] = True
            yield item
            return


        yield scrapy.Request(
                    url='https://www.farpost.ru/vladivostok/service/internet',
                    cookies=self.cookies,
                    headers=self.headers,
                    dont_filter=True,
                    callback=self.parse,
            )


