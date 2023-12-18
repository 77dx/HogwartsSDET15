from selenium.webdriver.chrome.webdriver import WebDriver
from web.base.login_base import LoginBase
from web.base.base_page import BasePage
from web.base.main_base import MainBase
from web.web_page.main_page import MainPage
from time import sleep
from common.log import log


class LoginPage(BasePage, LoginBase, MainBase):

    def input_account(self, driver, account):
        """
        输入用户名
        :param driver:
        :param account:
        :return:
        """
        account_locator = self.account_locator()
        log.info(f"输入用户名：{account}")
        return self.find(driver,"xpath", account_locator).send_keys(account)

    def input_password(self, driver, password):
        """
        输入密码
        :param driver:
        :param password:
        :return:
        """
        password_locator = self.password_locator()
        log.info(f"输入密码：{password}")
        return self.find(driver, "xpath", password_locator).send_keys(password)

    def click_submit_btn(self, driver):
        """
        点击登录按钮
        :param driver:
        :return:
        """
        submit_btn = self.login_button_locator()
        log.info("点击登录按钮")
        return self.find(driver,"xpath", submit_btn).click()

    def assert_login_success(self, driver):
        """
        断言是否登录成功
        :param driver:
        :return: 页面上是否出现发布订单按钮
        """
        pub_order_button = self.puborder_btn_locator()
        log.info("进行登录断言，断言结果下回再见")
        assert self.find(driver, "xpath", pub_order_button)

    def login_submit(self, driver:WebDriver, account, password):
        """
        登录操作，并断言是否登录成功
        :param driver:
        :param account:
        :param password:
        :return:
        """
        self.input_account(driver, account)
        self.input_password(driver, password)
        self.click_submit_btn(driver)
        self.assert_login_success(driver)
        sleep(3)
        return MainPage()

