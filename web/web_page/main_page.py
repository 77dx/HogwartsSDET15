from web.base.base_page import BasePage
from time import sleep

from web.web_page.order_list_page import OrderListPage
from web.web_page.pub_order_page import PubOrderPage
from common.log import log


class MainPage(BasePage):

    # 点击发布订单
    def publish_order_button(self, driver):
        # 处理弹窗广告
        # try:
        #     ele_pop = self.find(driver, "xpath", '//div[@class="close-icon"]')
        #     if ele_pop:
        #         ele_pop.click()
        # except Exception as e:
        #     log.error(e)
        # sleep(2)

        # 点击发布订单按钮
        self.find(driver, "xpath", '//a[@href="/placeorder"]').click()
        sleep(2)
        return PubOrderPage()

    # 订单列表
    def order_list(self, driver):
        self.find(driver, 'xpath','//*[@data-eventid="USER_2B_SITE_ORDER_ORDERLIST_CLICK"]').click()
        return OrderListPage()

