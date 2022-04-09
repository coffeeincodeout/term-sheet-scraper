import scrapy


class DealsSpider(scrapy.Spider):

    name = "deals"

    start_urls = [
        "https://fortune.com/newsletter/termsheet"
    ]

    def parse(self, response):

        data = response.xpath('//div/p')
        for items in data:
            # company_name = items.xpath('a/text()').get()
            # link = items.xpath('a/@href').get()
            if (company_name := items.xpath('a/text()').get()) is not None \
                    and (link := items.xpath('a/@href').get()) is not None:
                yield {
                    'name': company_name,
                    'url': link
                }

