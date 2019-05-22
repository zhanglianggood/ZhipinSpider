# -*- coding: utf-8 -*-
import scrapy
from ZhipinSpider.items import ZhipinspiderItem


class JobPositionSpider(scrapy.Spider):
    name = 'job_position'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c101280600-p100109/?page=1&ka=page-1']

    def parse(self, response):
        for each in response.xpath('//div[@class="job-list"]/ul//li'):
            item = ZhipinspiderItem()
            item['title'] = each.xpath('./div/div[@class="info-primary"]/h3/a/div[@class="job-title"]/text()').extract()[0]
            item['salary'] = each.xpath('./div/div[@class="info-primary"]/h3/a/span/text()').extract()[0]
            item['company'] = each.xpath('./div/div[@class="info-company"]/div/h3/a/text()').extract()[0]
            item['url'] = each.xpath('./div/div[@class="info-primary"]/h3/a/@href').extract()[0]
            item['work_addr'] = each.xpath('./div/div[@class="info-primary"]/p/text()').extract()[0]
            item['industry'] = each.xpath('./div/div[@class="info-company"]/div/p/text()').extract()[0]
            item['company_size'] = each.xpath('./div/div[@class="info-company"]/div/p/text()').extract()[-1]
            item['recruiter'] = each.xpath('./div/div[@class="info-publis"]/h3/text()').extract()[0]
            yield item
        next_pages = response.xpath('//div[@class="page"]/a[@class="next"]/@href').extract()
        if next_pages and len(next_pages) > 0:
            next_page = next_pages[0]
            print("---------------------", next_page)
            yield scrapy.Request("https://www.zhipin.com" + next_page, callback=self.parse)

