import scrapy
from ..items import FakePythonjobsItem, FakePythonjobsItemLoader


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    start_urls = ['https://realpython.github.io/fake-jobs/']

    def parse(self, response):
        jobs = response.xpath('//div[@id="ResultsContainer"]//div[@class="card"]')
        for job in jobs:
            job_item = FakePythonjobsItemLoader(item=FakePythonjobsItem(),
                                                     selector=job)
            job_item.add_xpath('job_name', './/h2/text()')
            job_item.add_xpath('company', './/h3/text()')
            job_item.add_xpath('location', './/p[@class="location"]/text()')
            job_item.add_xpath('date_posted', './/time/text()')
            job_item.add_xpath('apply_link', './/footer//a[2]/@href')

            yield job_item.load_item()
