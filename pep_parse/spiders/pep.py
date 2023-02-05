import scrapy

from ..items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        for row in response.css('table tr'):
            url = row.css('a::attr(href)').get()
            if not url:
                continue
            yield response.follow(
                url=url,
                callback=self.parse_pep,
                meta={
                    'number': row.css('td:nth-child(2) ::text').get(),
                    'name': row.css('td:nth-child(3) ::text').get()
                })

    def parse_pep(self, response):
        yield PepParseItem(
            number=response.request.meta['number'],
            name=response.request.meta['name'],
            status=response.css('abbr::text').get(),
        )
