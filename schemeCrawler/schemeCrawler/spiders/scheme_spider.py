import scrapy

from schemeCrawler.items import SchemeItem

class SchemeSpider(scrapy.Spider):
    name = "schemeSpider"
    start_url = "http://www.tn.gov.in"
    allowed_domains = ["tn.gov.in"]
    start_urls = [
        "http://www.tn.gov.in/scheme"
    ]

    def parse(self, response):
        for href in response.xpath('//p/a/@href'):
           url = response.urljoin(href.extract())
           yield scrapy.Request(url, callback=self.parse_dept_contents)
        href = response.xpath("//a[contains(@title,'Go to next page')]/@href")
        url = response.urljoin(self.start_url + "".join(href.extract()))
        if url:
            yield scrapy.Request(url, callback=self.parse)


    def parse_dept_contents(self, response):
        for href in response.xpath('//p/a/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_scheme_contents)
        href = response.xpath("//a[contains(@title,'Go to next page')]/@href")
        url = response.urljoin(self.start_url + "".join(href.extract()))
        if url:
            yield scrapy.Request(url, callback=self.parse_dept_contents)

    def parse_scheme_contents(self,response):
        item = SchemeItem()
        for sel in response.xpath("//div[contains(@class,'node_viewlist')]"):

            key = ''.join(sel.xpath("span[contains(@class,'left_column')]/text()").extract())
            value = ''.join(sel.xpath("span[contains(@class,'right_column')]/text()").extract())

            if key == 'Concerned Department':
                item['department'] = value
            if key == 'Concerned District':
                item['district'] = value
            if key == 'Title / Name':
                item['name'] = value
            if key == 'Beneficiaries':
                item['beneficiaries'] = value
            if key == 'How To Avail':
                item['how_to_avail'] = value
            if key == 'Introduced On':
                item['valid_from'] = value
            if key == 'Valid Upto':
                item['valid_till'] = value
            if key == 'Description':
                item['description'] = value
            if key == 'Age':
                item['eligible_age'] = value
            if key == 'Income':
                item['eligible_income'] = value
            if key == 'Community':
                item['eligible_community'] = value
            if key == 'Other Details':
                item['eligible_other_details'] = value

        yield item




