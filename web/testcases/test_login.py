import pytest
from web.web_page.index_page import IndexPage

user_list = [
    {"account": "13366666666", "password": "test@123456"},
    {"account": "13311111111", "password": "test@123456"},
    {"account": "13377777777", "password": "test@123456"}
]
class TestLogin:

    @pytest.mark.parametrize("user", user_list)
    def test_login_success(self, chrome_driver, user):
        IndexPage().goto_loginPage(chrome_driver).\
            login_submit(chrome_driver, user["account"], user["password"])
