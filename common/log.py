"""
@ Title: 封装日志方法
@ Author: Cathy
@ Time: 2023/12/6 15:37
"""
import logging
import os
import time

from common.tools import get_project_path, sep


def set_log(logger_name, log_level):
    # 创建logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)
    log_path = sep([get_project_path(), "logs","autotest_web_logs"], False, True)

    # 若日志目录不存在，则自动创建
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    # 设置日志文件名格式： 日志绝对路径 + 生成日志时间.log
    local_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    log_name = log_path + local_time + ".log"

    # 创建handler，写入日志信息
    fh_info = logging.FileHandler(log_name)
    fh_info.setLevel(log_level)

    # 定义日志输出格式
    log_format = logging.Formatter("%(asctime)s - %(filename)s - %(module)s - %(funcName)s -%(lineno)d - %(levelname)s - %(message)s")
    fh_info.setFormatter(log_format)

    # 给logger添加handler
    logger.addHandler(fh_info)

    return logger


log = set_log("web自动化测试", logging.DEBUG)







if __name__ == '__main__':
    log.debug("I am debug")
    log.info("I am info")

