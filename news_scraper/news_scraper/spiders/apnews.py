from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class APNewsSpider(CrawlSpider):
    name = 'apnews_spider'
    allowed_domains = ['apnews.com']
    start_urls = ['https://apnews.com/']

    rules = (
        Rule(LinkExtractor(allow=r'/article/'), callback='parse_article', follow=True),
    )

    def parse_article(self, response):
        yield {
            'url': response.url,
            'title': response.css('h1::text').get(),
            'author': response.css('span.Component-bylines-0-2-38::text').get(),
            'date': response.css('span.Component-datePublished-0-2-39::text').get(),
            'content': ' '.join(response.css('div.Article p::text').getall()),
        }
