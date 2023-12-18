"""
@ Title: 在allure生成的测试报告中增加测试过程/结果图片
@ Author: Cathy
@ Time: 2023/12/6 12:28
"""
import allure
from time import sleep


def add_img_to_report(driver, step_name, need_sleep=True):
    """
    在测试过程中截图并将其插入 allure 测试报告中
    :param driver:
    :param step_name:
    :param need_sleep:
    :return:
    """
    if need_sleep:
        sleep(2)

    allure.attach(driver.get_screenshot_as_png(), step_name + ".png", allure.attachment_type.PNG)


def add_img_path_to_report(img_path, step_name):
    """
    将图片以附件的形式插入 allure 测试报告中
    :param img_path:
    :param step_name:
    :return:
    """
    allure.attach.file(img_path, step_name, allure.attachment_type.PNG)