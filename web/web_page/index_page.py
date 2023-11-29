from web.base.base_page import BasePage
from web.web_page.login_page import LoginPage


class IndexPage(BasePage):

    def goto_loginPage(self, driver):
        base_url = 'https://test-www.wanshifu.com'
        driver.get(base_url)
        self.find(driver, 'xpath', '//*[@class="wshifu-user-login wshifu-user-button"]').click()
        return LoginPage()