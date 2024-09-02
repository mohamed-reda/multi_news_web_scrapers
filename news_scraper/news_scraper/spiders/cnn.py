from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CNNSpider(CrawlSpider):
    name = 'cnn_spider'
    allowed_domains = ['edition.cnn.com']
    start_urls = ['https://edition.cnn.com/']

    rules = (
        Rule(LinkExtractor(allow=r'/\d{4}/\d{2}/\d{2}/'), callback='parse_article', follow=True),
    )

    def parse_article(self, response):
        yield {
            'url': response.url,
            'title': response.css('h1.headline__text::text').get(),
            'author': self.extract_author(response),
            'date': response.css('div.timestamp::text').get(),
            'content': ' '.join(response.css('div.article__content p::text').getall()),
        }

    def extract_author(self, response):
        authors = response.css('div.byline__names span.byline__name::text').getall()
        if authors:
            return ', '.join(author.strip() for author in authors if author.strip())
        return None
