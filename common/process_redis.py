"""
@ Title:
@ Author: Cathy
@ Time: 2023/12/18 16:51
"""
from common.redis_operation import RedisOperation
from common.tools import get_now_time


class Process:
    def __init__(self):
        self.redis_client = RedisOperation().redis_client
        self.UI_AUTOTEST_PROCESS = "ui_autotest_process"
        self.FAILED_TESTCASE_NAMES = "failed_testcase_names"
        self.RUNNER_STATUS = "running_status"

    def reset_all(self):
        # 删除所有进度
        self.redis_client.delete(self.UI_AUTOTEST_PROCESS)
        # 删除所有失败用例的名称
        self.redis_client.delete(self.FAILED_TESTCASE_NAMES)

    def init_process(self,total):
        """
        初始化进度，总数，成功数，失败数，开始时间，运行状态
        :param total: 测试用例总数
        :return:
        """
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS,"total", total)
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "success", 0)
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "fail", 0)
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "start_time", get_now_time())
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "end_time", "")
        self.redis_client.set(self.RUNNER_STATUS, 1)

    def update_success(self):
        self.redis_client.hincrby(self.UI_AUTOTEST_PROCESS, "success")

    def update_fail(self):
        self.redis_client.hincrby(self.UI_AUTOTEST_PROCESS,"fail")

    def insert_into_fail_testcase_names(self, fail_testcase_name):
        self.redis_client.lpush(self.FAILED_TESTCASE_NAMES, fail_testcase_name)

    def get_process(self):
        """
        获取进度，计算百分比
        :return:
        """
        total, success,fail, _= self.get_result()
        if total == 0:
            return 0
        else:
            result = "%.1f" %((int(success) + int(fail)) / int(total) * 100) + "%"
        return result


    def get_result(self):
        """
        获取测试结果
        :return:
        """
        total = self.redis_client.hget(self.UI_AUTOTEST_PROCESS, "total")
        if total is None:
            total = 0
        success = self.redis_client.hget(self.UI_AUTOTEST_PROCESS, "success")
        if success is None:
            success = 0
        fail = self.redis_client.hget(self.UI_AUTOTEST_PROCESS, "fail")
        if fail is None:
            fail = 0
        start_time = self.redis_client.hget(self.UI_AUTOTEST_PROCESS, "start_time")
        if start_time is None:
            start_time = '-'
        return total, success, fail, start_time