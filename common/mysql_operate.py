"""
@ Title: 连接mysql
@ Author: Cathy
@ Time: 2023/12/7 14:59
"""
import pymysql

from common.yaml_config import GetYamlConf


class MysqlOperate:

    def __init__(self):
        data = GetYamlConf().get_mysql()
        self.db = data["db"]
        self.port = data["port"]
        self.user = data["user"]
        self.password = data["password"]
        self.host = data["host"]
        self.cursor = None
        self.conn = None

    def __conn_mysql(self):
        try:
            self.conn = pymysql.connect(user=self.user,password=self.password,db=self.db,port=self.port,host=self.host, charset="utf8mb4")
        except Exception as e:
            print(e)
            return False
        self.cursor = self.conn.cursor()
        return True

    def __close_mysql(self):
        self.cursor.close()
        self.conn.close()

    def __commit(self):
        self.conn.commit()
        return True

    def query(self, sql):
        self.__conn_mysql()
        self.cursor.execute(sql)
        query_data = self.cursor.fetchall()
        if query_data ==():
            query_data = None
            print(f"{sql}查询结果为空")
        self.__close_mysql()
        return query_data




if __name__ == '__main__':
    print(MysqlOperate().query("select * from auto_test_user"))




