from web.web_page.index_page import IndexPage
from web.web_page.main_page import MainPage
from web.testcases.test_login import TestLogin
from web.web_page.pub_order_page import PubOrderPage
import pytest
import allure


class TestPubOrder:
    @pytest.mark.puborder
    @allure.feature("发布订单")
    @allure.description("本地上传图片，发布订单")
    def test_pub_order_local_img(self, chrome_driver):
        """发布订单，本地上传图片"""
        with allure.step("登录"):
            TestLogin().test_login_success_pre(chrome_driver)

        with allure.step("点击发布订单"):
            MainPage().publish_order_button(chrome_driver)

        with allure.step("填写订单信息，并提交订单"):
            PubOrderPage().pub_category_jiaju(chrome_driver)


