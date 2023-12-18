"""
@ Title: 连接redis
@ Author: Cathy
@ Time: 2023/12/18 15:09
"""
from common.yaml_config import GetYamlConf
import redis


class RedisOperation:
    def __init__(self):
        redis_info = GetYamlConf().get_redis()
        self.redis_client = redis.Redis(
            host = redis_info["host"],
            port = redis_info["port"],
            db = redis_info["db"],
            decode_responses=True,
            charset="UTF-8",
            encoding="UTF-8"
            # password=user:password       #  账号密码
        )

if __name__ == '__main__':
    print(RedisOperation().redis_client.get("username"))