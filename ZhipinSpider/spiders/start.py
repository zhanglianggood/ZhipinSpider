from scrapy import cmdline

try:
    cmdline.execute('scrapy crawl job_position'.split())
except Exception as e:
    print(e)