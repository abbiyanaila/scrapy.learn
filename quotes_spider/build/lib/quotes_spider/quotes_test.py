from scrapy import Spider
from scrapy.http import Request

class QuoteSpider(Spider):
    name = 'quotes'
    allowed_domain = ['quotes.toscrape.com']
    start_url = (
        'https://quotes.toscrape.com/'
    )

    def parse(self, response):
        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
            text = quote.xpath()