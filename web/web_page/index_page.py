from web.base.base_page import BasePage
from web.web_page.login_page import LoginPage
from common.yaml_config import GetYamlConf
from time import sleep


class IndexPage(BasePage):

    def goto_loginPage(self, driver):
        base_url = 'https://www.wanshifu.com'
        # base_url = GetYamlConf().env["pre_url"]
        driver.get(base_url)
        sleep(3)
        self.find(driver, "xpath", '//a[@class="wshifu-user-login wshifu-user-button"]').click()
        return LoginPage()

