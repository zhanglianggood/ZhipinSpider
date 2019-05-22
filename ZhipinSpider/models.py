import sqlalchemy
from sqlalchemy import Column, Integer, Float, String, DATE
from connect import BASE, ConnectMySql


class ZhiPin(BASE):
    __tablename__ = "job_position"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    salary = Column(String(50))
    company = Column(String(200))
    url = Column(String(100))
    work_addr = Column(String(200))
    industry = Column(String(20))
    company_size = Column(String(50))
    recruiter = Column(String(50))
    publish_time = Column(DATE)


try:
    conn = ConnectMySql()
    BASE.metadata.create_all(conn.connMySql())
except Exception as e:
    print("创建表失败：", e)
    raise
