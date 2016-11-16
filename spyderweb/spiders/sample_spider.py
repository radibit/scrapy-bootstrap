from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from spyderweb.items import SampleModel


class SampleCrawlerSpider(CrawlSpider):
    name = "samplecrawler"
    allowed_domains = ['example.com']
    start_urls = [
        'https://www.example.com/category'
    ]

    rules = (
        # Extract links matching 'page=' from a span with data-href attribute
        # and follow links (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=('page='), tags=('span'), attrs=('data-href') )),

        # Extract links matching 'en/item' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow='en/item'), callback='parse_item'),
    )

    def parse_item(self, response):
        self.logger.info('Hey, we found a page! %s', response.url)

        item = SampleModel()
        item['headline'] = response.xpath('//h1/text()').extract()

        return item
