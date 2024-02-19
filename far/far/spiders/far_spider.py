import scrapy
import json
import re


class Captcha(scrapy.Spider):
    name = 'book'
    allowed_domains = ['www.farpost.ru']
    start_urls = ['http://www.farpost.ru/']
    #handle_httpstatus_list = [404, 502, 503]


    cookie = {
        'ring': 'dde278d3c21bd2cbd802cbf2144315a0',
        'city':'1',
        '_ga_64RVG4FR1N':'GS1.2.1708066858.10.0.1708066858.0.0.0',
        '_ga': 'GA1.1.596243486.1698948002',
        'boobs':'c24ec411e5d0b462de3a11d125d70f0141d8ca1be377d12cd51a8ac77f098b11ufaa0f9',
        'pony':'4d5459304d6a55794d446b3du73a0682ff39e412e650749d641aa0a88',
        '_ga_G0RWKN84TQ':'GS1.1.1708170834.14.0.1708170834.60.0.0',
        #'sentinel':'CWOb4vTPf2EjdEir/BvHcjXrOt0TwLfJ1lS98r5thwyzLO6nFfwOTlSKtw9g9JA5XbR7d0uwz+9FbNCNYK82T8tZ4TxAxqr5V7aOVqc99WM=:17HEYCrURuY39xwicV9JHwksTeX16+LL/LY5EY7FnNo='
    }

    header = {
        'Host': 'www.farpost.ru',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Ch-Ua': '"Chromium";v="121", "Not A(Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Full-Version': '""',
        'Sec-Ch-Ua-Arch': '""',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Ch-Ua-Platform-Version': '""',
        'Sec-Ch-Ua-Model': '""',
        'Sec-Ch-Ua-Bitness': '""',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Priority': 'u=0, i'
    }


    def __init__(self):
        super(Captcha, self).__init__()

    def start_requests(self):
        for i in range(100):
            yield scrapy.Request(
                    url='https://www.farpost.ru',
                    cookies=self.cookie,
                    headers=self.header,
                    dont_filter=True,
                    callback=self.parse,
            )


    # Метод сбора основных данных
    def parse(self, response):
        r = response.css('title::text').extract()
        print(r)

