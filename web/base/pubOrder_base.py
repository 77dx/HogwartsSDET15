"""
@ Title:
@ Author: Cathy
@ Time: 2023/12/12 15:29
"""


class PubOrderBase:

    def select_service_category(self, num):
        """
        选择服务类目
        :param num: 选择第几个类目，从1-15
        :return:
        """
        return "//span[@class='level-content flex-size']/li[" + num + "]"

    def switch_category_pop(self):
        """
        切换类目的确认弹窗
        :return:
        """
        return '//button[@class="ant-btn ant-btn-primary sure-btn"]'

    def service_types(self):
        """
        获取该类目的所有服务类型
        :return:
        """
        return '/span[@class="level-content"]'




