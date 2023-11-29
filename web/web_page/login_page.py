from selenium.webdriver.chrome.webdriver import WebDriver
from web.base.login_base import LoginBase
from web.base.base_page import BasePage
from web.web_page.main_page import MainPage
from time import sleep


class LoginPage(BasePage,LoginBase):

    def input_account(self, driver, account):
        account_locator = self.account_locator()
        return self.find(driver,"xpath",account_locator).send_keys(account)


    def input_password(self, driver, password):
        password_locator = self.password_locator()
        return self.find(driver, "xpath", password_locator).send_keys(password)

    def click_submit_btn(self, driver):
        submit_btn = self.login_button_locator()
        return self.find(driver, "xpath",submit_btn).click()


    def login_submit(self, driver:WebDriver, account, password):
        self.input_account(driver, account)
        self.input_password(driver, password)
        self.click_submit_btn(driver)
        sleep(3)
        return MainPage()






    # def submit(self, driver, file, title):
    #     self.parse_yaml(driver, file, title)
    #     return MainPage()