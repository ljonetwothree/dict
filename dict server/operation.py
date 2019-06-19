"""
dict 数据库处理
功能：提供服务端的所有数据库操作
"""
import pymysql
import hashlib
SALT="##@@##"


class Database:
    def __init__(self,host='localhost',port=3306,user='root',passwd='123456',charset='utf8',database='dict'):
        self.host=host
        self.port=port
        self.user=user
        self.passwd=passwd
        self.database=dict
        self.charset=charset
        self.connect_db() #链接数据库

    # 链接数据库
    def connect_db(self):
        self.db=pymysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.passwd,database=self.database,charset=self.charset)

    # 创建游标
    def create_cursor(self):
        self.cur=self.db.cursor()


    #关闭数据库
    def close(self):
        self.db.close()

    #注册操作
    def register(self,name,passwd):
        sql="select * from user where name='%s"%name
        self.cur.execute(sql)
        r=self.cur.fetchone()
        if r:
            return False
        else:
        #密码加密处理
            hash=hashlib.md5((name+SALT).encode())
            hash.update(passwd.encode())
            passwd=hash.hexdigest()
            sql="insert into user (name,passwd) values (%s,%s)"
            try:
                self.cur.execute(sql,[name,passwd])
                self.db.commit()
                return True
            except Exception:
                self.db.rollback()
                return False
