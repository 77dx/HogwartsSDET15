from web.web_page.index_page import IndexPage
from web.testcases.test_login import TestLogin
import pytest

class TestPubOrder:

    def test_pub_order_success(self,chrome_driver):
        IndexPage().goto_loginPage(chrome_driver).submit(chrome_driver).\
            publish_order_button(chrome_driver).pub_local_good(chrome_driver)

    @pytest.mark.test01
    def test_01(self, chrome_driver):
        TestLogin().test_login_success(chrome_driver)