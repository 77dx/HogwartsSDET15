from web.base.base_page import BasePage
from time import sleep

from web.web_page.order_list_page import OrderListPage
from web.web_page.pub_order_page import PubOrderPage


class MainPage(BasePage):

    # 发布订单
    # @DecoPopAd(driver)
    def publish_order_button(self, driver):
        # 点击发布订单按钮
        self.parse_yaml(driver, 'main_page.yaml','publish_order')
        sleep(2)
        return PubOrderPage()

    # 订单列表
    def order_list(self, driver):
        self.find(driver, 'xpath','//*[@data-eventid="USER_2B_SITE_ORDER_ORDERLIST_CLICK"]').click()
        return OrderListPage()

