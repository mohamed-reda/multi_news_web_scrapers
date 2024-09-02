from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class YahooNewsSpider(CrawlSpider):
    name = 'yahoo_news_spider'
    allowed_domains = ['news.yahoo.com']
    start_urls = ['https://news.yahoo.com/']

    rules = (
        Rule(LinkExtractor(allow=r'/.+-\d+\.html'), callback='parse_article', follow=True),
    )

    def parse_article(self, response):
        yield {
            'url': response.url,
            'title': response.css('h1::text').get(),
            'author': response.css('span.caas-author-byline-collapse::text').get(),
            'date': response.css('time::attr(datetime)').get(),
            'content': ' '.join(response.css('div.caas-body p::text').getall()),
        }
