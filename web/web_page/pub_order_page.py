from time import sleep
from web.base.base_page import BasePage
import os
import random


class PubOrderPage(BasePage):

    def pub_order_success(self, driver):

        # 页面下滑到选择商品处
        ele = self.find(driver, 'xpath', '//*[@class="prefix-desc required"]')
        driver.execute_script("arguments[0].scrollIntoView();", ele)
        sleep(2)

        # 点击商品库添加
        self.find(driver, 'xpath', '//*[@class="start-add-goods-placeorder"]').click()
        self.find(driver, 'css', '.ant-checkbox-input:nth-child(1)').click()
        self.find(driver, 'xpath', '//span[text()="确 定"]').click()

        js = "window.scrollBy(0,-500)"
        driver.execute_script(js)
        self.find(driver, 'xpath', '//*[@class="anticon anticon-plus"]').click()

    def pub_local_good(self, driver):
        try:
            '''
            下单第一页
            '''
            # 选择服务类目,服务类型,下单模式
            self.find(driver, 'xpath','//span[@class="level-content flex-size"]/li[1]').click()
            # 如果提示确认是否更换类目的弹窗，点击确认
            sleep(1)
            element_sure_btn = self.find(driver, 'xpath', '//button[@class="ant-btn ant-btn-primary sure-btn"]')
            print(f"这是确认切换类目的弹窗:{element_sure_btn}")
            if element_sure_btn:
                element_sure_btn.click()
            self.find(driver, 'xpath', '//span[text()="安装"]').click()
            self.find(driver, 'xpath', '//span[text()="商家支付"]').click()
            sleep(1)
            self.find(driver, 'xpath', '//span[text()="报价招标"]').click()

            # 页面下滑至选择商品处
            ele = self.find(driver, 'xpath','//div[@class="start-add-goods-placeorder"]')
            driver.execute_script("arguments[0].scrollIntoView();",ele)
            sleep(2)

            # 选择商品
            self.find(driver, 'xpath','//div[@class="ant-row ant-legacy-form-item common-item common-category"]').click()
            sleep(3)
            self.find(driver, 'xpath', '//*[text()="床类"]').click()
            self.find(driver, 'xpath','//*[text()="布艺床"]').click()
            sleep(2)

            # 选择本地上传
            root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            file_path = root_dir + '/web/resource/img/aa.jpeg'
            self.find(driver, 'xpath','//input[@type="file"]').send_keys(file_path)
            sleep(3)

            # 页面滚动，显示出商品属性字段
            self.srolled_element_into_view(driver, 'xpath','//input[@id="Step1_45002998-0"]')
            # 选择商品属性
            self.find(driver, 'xpath','//input[@id="Step1_45002998-0"]').click()
            sleep(1)
            self.find(driver, 'xpath', '//div[@class="ant-select-item-option-content"]').click()
            self.find(driver, 'xpath', '//input[@id="Step1_86679802-0"]').click()
            self.find(driver, 'xpath', '//div[@id="86679806"]').click()
            sleep(1)

            # 点击下一页
            self.find(driver, 'xpath', '//div[@class="next-btn"]').click()

            '''
            下单第二页
            '''
            # 输入地址
            self.find(driver, 'xpath', '//textarea[@name="aiaddress"]').send_keys(f'万某某{random.randint(1,999)}，13612345678，广东省深圳市宝安区某街道某某路某花园')
            # 点击立即识别
            self.find(driver, 'xpath', '//a[@class="ml-10"]').click()
            sleep(1)

            # 选择已到货
            self.finds(driver, 'xpath', '//input[@name="customArriveStatus"]')[0].click()
            sleep(1)

            # 点击提交订单
            self.finds(driver, 'xpath', '//div[@class="next-wrapper"][1]//button[@type="submit"]')[1].click()
            sleep(3)

        except Exception as e:
            raise e
