import pytest
import allure
from web.web_page.index_page import IndexPage

user_list = [
    {"account": "17688968877", "password": "Cathy8877"},
    {"account": "18740778077", "password": "Cathy8877"}
]
class TestLogin:

    @pytest.mark.parametrize("user", user_list)
    def test_login_success(self, chrome_driver, user):
        with allure.step("登录"):
            IndexPage().goto_loginPage(chrome_driver).\
                login_submit(chrome_driver, user["account"], user["password"])
