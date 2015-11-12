import scrapy

class SchemeSpider(scrapy.Spider):
    name = "schemeSpider"
    allowed_domains = ["tn.gov.in"]
    start_urls = [
        "http://www.tn.gov.in/scheme"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)