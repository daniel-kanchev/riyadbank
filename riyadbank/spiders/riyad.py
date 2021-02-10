import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from datetime import datetime
from riyadbank.items import Article


class RiyadSpider(scrapy.Spider):
    name = 'riyad'
    start_urls = ['https://www.riyadbank.com/ar/media-center/press-releases']

    def parse(self, response):
        links = response.xpath('//article[@class="post"]//h2/a/@href').getall()
        yield from response.follow_all(links, self.parse_article)

        next_page = response.xpath('//li[@class="nextlist"]/a/@href').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_article(self, response):
        item = ItemLoader(Article())
        item.default_output_processor = TakeFirst()

        title = response.xpath('//h1/text()').get().strip()
        date = response.xpath('//time/text()').get().strip()
        content = response.xpath('//div[@class="text-holder"]//text()').getall()
        content = [text for text in content if text.strip()]
        content = "\n".join(content).strip()

        item.add_value('title', title)
        item.add_value('date', date)
        item.add_value('link', response.url)
        item.add_value('content', content)

        return item.load_item()
