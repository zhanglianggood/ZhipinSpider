from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from scrapy.conf import settings

BASE = declarative_base()


class ConnectMySql(object):
    def __init__(self):
        try:
            self.host = settings["MYSQL_HOST"]
            self.port = settings["MYSQL_PORT"]
            self.user = settings["MYSQL_USER"]
            self.passwd = settings["MYSQL_PASS"]
            self.database = settings["MYSQL_DATABASE"]
        except Exception as e:
            print(e)
            raise ImportError("\033[41;1m请配置数据库连接参数033[0m")

    def connMySql(self):
        connStr = "mysql+pymysql://" + self.user + ":" + self.passwd + "@" + self.host + "/" + self.database
        engine = create_engine(connStr, encoding="utf-8", echo=False)
        return engine
