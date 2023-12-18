from time import sleep

import pytest
import allure
from web.web_page.index_page import IndexPage
from common.report_add_img import add_img_to_report
from common.log import log
from common.yaml_config import GetYamlConf
from web.web_page.login_page import LoginPage

user_list = [
    {"account": "18740778077", "password": "Cathy8877"}
]

@allure.epic("登录测试")
class TestLogin:
    @pytest.mark.login
    @pytest.mark.parametrize("user", user_list)
    @allure.feature("登录成功")
    @allure.description("登录成功测试")
    def test_login_success_online(self, chrome_driver, user):
        """使用pytest参数化入参，测试正常登录场景"""
        with allure.step("登录"):
            IndexPage().goto_loginPage(chrome_driver).\
                login_submit(chrome_driver, user["account"], user["password"])
            sleep(3)
            add_img_to_report(chrome_driver, "登录成功")
            log.info("点击登录按钮后，进行截图")

    @pytest.mark.pre_login
    @allure.feature("pre环境登录成功")
    @allure.description("pre环境登录成功测试")
    def test_login_success_pre(self, chrome_driver):
        """使用pytest参数化入参，测试正常登录场景"""
        with allure.step("pre环境登录"):
            data = GetYamlConf("testdata.yaml").env["prod_users"]["cathy"]
            IndexPage().goto_loginPage(chrome_driver)
            LoginPage().login_submit(chrome_driver, data["username"], data["password"])
            add_img_to_report(chrome_driver, "pre环境登录成功")
            log.info("点击登录按钮后，进行截图")

    @pytest.mark.login
    @allure.feature("登录失败")
    @allure.description("登录失败测试")
    def test_login_fail(self, chrome_driver):
        """使用无法登录的用户"""
        with allure.step("登录失败测试"):
            data = GetYamlConf("testdata.yaml").env["prod_users"]["bad_user"]
            IndexPage().goto_loginPage(chrome_driver)
            LoginPage().login_submit(chrome_driver, data["username"], data["password"])
            add_img_to_report(chrome_driver, "登录失败")
            log.info("点击登录按钮后，进行截图")