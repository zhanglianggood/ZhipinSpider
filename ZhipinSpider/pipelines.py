# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from connect import ConnectMySql
from sqlalchemy.orm import sessionmaker
from models import ZhiPin
import time


class ZhipinspiderPipeline(object):
    def __init__(self):
        try:
            conn = ConnectMySql()
            self.sessions = sessionmaker(bind=conn.connMySql())()
        except Exception as e:
            print("\033[42;1mDataBase init Failed!\033[0m", e)
            raise ConnectionError("数据库初始化失败")
        # self.json_file = open("zhipin.txt", "w", encoding="utf-8")
        # self.json_file.write("[\n")

    def close_spider(self, spider):
        self.sessions.commit()
        print("数据提交完成")
        # self.json_file.seek(-2, 1)
        # self.json_file.write('\n]')
        # self.json_file.close()

    def process_item(self, item, spider):
        job_obj = ZhiPin()
        for k, v in item.items():
            if hasattr(job_obj, k):
                setattr(job_obj, k, v)
                # job_obj.__setattr__(k, v)
                # print(getattr(job_obj, k))
                # time.sleep(1)
            else:
                raise KeyError("不需要提取该数据：", k)
        try:
            self.sessions.add(job_obj)
        except ConnectionError as e:
            print("数据插入数据库失败", e)
        # print(item)
        # text = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        # self.json_file.write(text)
        # print('工作名称：', item['title'])
        # print('薪资范围：', item['salary'])
        # print('招聘公司：', item['company'])
        # print('工作详细信息：', item['url'])
        # print('工作地址：', item['work_addr'])
        # print('公司行业：', item['industry'])
        # print('公司规模：', item['company_size'])
        # print('招聘人：', item['recruiter'])
        return item
