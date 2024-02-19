import sqlite3
from far.far.spiders import far_spider
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging




urlList = []


parserConfig = CrawlerRunner(settings={'DOWNLOAD_DELAY': 0, 'ROBOTSTXT_OBEY': False})



@defer.inlineCallbacks
def genreParser():
    yield parserConfig.crawl(far_spider.Captcha)


genreParser()
# getUser()

reactor.run()

