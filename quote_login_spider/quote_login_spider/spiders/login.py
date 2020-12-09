import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['quote.toscrape.com']
    start_urls = (
        'https://quotes.toscrape.com/login',
        )

    def parse(self, response):
        csrf_token = response.xpath(
            '//*[@name="csrf_token"]/@value').extract_first()


        yield FormRequest('https://quotes.toscrape.com/login',
                        formdata = {'csrf_token': csrf_token,
                                    'username': 'abbiyanaila',
                                    'password': '191618'},
                        callback = self.parse_after_login)

    def parse_after_login(self, response): 
        open_in_browser(response)  
        # if response.xpath('//a[text()="Logout"]'):
        #     self.log('You logged in!')
        # pass
