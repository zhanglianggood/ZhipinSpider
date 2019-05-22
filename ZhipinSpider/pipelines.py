# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ZhipinspiderPipeline(object):
    def process_item(self, item, spider):
        print('工作名称：', item['title'])
        print('薪资范围：', item['salary'])
        print('招聘公司：', item['company'])
        print('工作详细信息：', item['url'])
        print('工作地址：', item['work_addr'])
        print('公司行业：', item['industry'])
        print('公司规模：', item['company_size'])
        print('招聘人：', item['recruiter'])
        # return item
