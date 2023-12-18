"""
@ Title: 操作yaml
@ Author: Cathy
@ Time: 2023/12/7 11:14
"""
import yaml
from common.tools import get_project_path,sep


class GetYamlConf:
    def __init__(self, yaml_file="environment.yaml"):
        with open(get_project_path() + sep(["web", "data_yaml", yaml_file], True),"r", encoding="utf-8") as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)

    def get_mysql(self):
        mysql_env = self.env["mysql"]
        return mysql_env

    def get_redis(self):
        redis_env = self.env["redis"]
        return redis_env




if __name__ == '__main__':
    g = GetYamlConf()
    # print(g.get_redis())
