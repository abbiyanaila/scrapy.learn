import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = (
        'https://quotes.toscrape.com/',
    )

    def parse(self, response):
        # h1_tag = response.xpath('//h1/a/text()').extract_first()
        # tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()
        # yield {'H1_Tag': h1_tag, 'Tags': tags}
        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
            text = quote.xpath('.//*[@class="text"]/text()').extract_first()
            author = quote.xpath('.//*[@itemprop="author"]/text()').extract_first()
            tags =  quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first()

            yield{'Text': text,
                'Author': author,
                'Tags': tags}
                    
        
        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoint(next_page_url,href.extract())
        yield scrapy.Request(absolute_next_page_url)
    


