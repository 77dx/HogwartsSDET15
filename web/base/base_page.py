import datetime
import os

from selenium.common import ElementNotVisibleException, WebDriverException, StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from common.tools import get_img_path
import time
import yaml




class BasePage():
    # def __init__(self, driver):
    #     # 创建driver
    #     self.driver = driver
    #
    #     # 设置全局的隐士等待
    #     self.driver.implicitly_wait(10)
    #     if self.base_url != "":
    #         self.driver.get(self.base_url)
    def find(self, driver, locate_type, locator_expression=None):
        try:
            if locator_expression is None:
                result = driver.find_element(*locate_type)
            else:
                if locate_type == "xpath" or locate_type == "XPATH":
                    result = driver.find_element(By.XPATH, locator_expression)
                elif locate_type == "css" or locate_type == "CSS":
                    result = driver.find_element(By.CSS_SELECTOR, locator_expression)
            print(result)
            return result
        except Exception as e:
            print(f'没有定位到元素{e}')
            return False

    def finds(self, driver, locate_type, locator_expression):
        return driver.find_elements(locate_type, locator_expression)

    def parse_yaml(self, driver, fileName,func_name):
        with open("../data_yaml/" + fileName, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        self.parse(driver, data[func_name])

    def parse(self, driver, steps):
        for step in steps:
            if 'click' == step.get("action"):
                print("进来点击事件")
                self.find(driver, step.get("by"), step.get("locator")).click()
            elif 'send' == step.get("action"):
                print("进来输入事件")
                self.find(driver, step.get("by"),step.get("locator")).send_keys(step.get("content"))
                # self.element_fill_value(step["by"], step["locator"], step["content"])
    # 动态导入，还未实现
    # module_name = step.get("gotoPage")
    # importlib.import_module(module_name, base="web.web_page")
    # return eval(module_name)(self.driver)

    def srolled_element_into_view(self, driver, locate_type, locator_expression):
        self.find(driver, locate_type, locator_expression).location_once_scrolled_into_view

    def wait_for_ready_state_complete(self, driver, timeout=30):
        """
        等待页面完全加载完成
        :param timeout: 超时时间
        :return:
        """
        start_ms = time.time() * 1000
        stop_ms = start_ms + (timeout * 1000)
        for x in range(int(timeout * 10)):
            try:
                ready_state = driver.execute_script("return document.readyState")
            except WebDriverException:
                time.sleep(0.03)
                return True
            if ready_state == "complete":
                time.sleep(0.03)
                return True
            else:
                if time.time() *1000 >= stop_ms:
                    break
                time.sleep(0.1)
        raise Exception(f"页面未在{timeout}内加载完成")


    def element_appear(self, driver, locate_type, locator_expression,timeout=30):
        """
        等待元素出现
        :param locate_type: 定位方式
        :param locator_expression: 定位表达式
        :param timeout: 超时时间
        :return:
        """
        if locate_type:
            start_ms = time.time() * 1000
            stop_ms = start_ms + (timeout * 1000)
            for x in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locate_type, value=locator_expression)
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
                except Exception:
                    if time.time() * 1000 >= stop_ms:
                        break
                    time.sleep(0.1)
            raise ElementNotVisibleException(f"元素未出现,定位方式{locate_type}，定位表达式{locator_expression}")

    def append_return(self, driver, fill_value, element):
        if not fill_value.endwith("\n"):
            element.send_keys(fill_value)
        else:
            fill_value = fill_value[:-1]
            element.send_keys(fill_value)
            element.send_keys(Keys.RETURN)
        self.wait_for_ready_state_complete(driver)

    def element_fill_value(self, driver, locate_type, locator_expression, fill_value, timeout=30):
        """
        输入框填值
        1.输入框是否可见
        2.清除输入框
        3.需要将填入的值转换成字符串
        4.填入的值以\n结尾，操作需要回车
        5.填入值后需等待页面元素加载完成
        :param locate_type:
        :param locator_expression:
        :return:
        """
        element = self.element_appear(locate_type,locator_expression,timeout)
        try:
            element.clear()
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver, timeout)
            element = self.element_appear(locate_type, locator_expression, timeout)
            try:
                element.clear()
            except Exception:
                pass
        except Exception:
            pass
        fill_value_type = type(fill_value)
        if fill_value_type is int or fill_value_type is float:
            fill_value = str(fill_value)
        try:
            self.element_appear(locate_type, locator_expression, timeout)
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver)
            time.sleep(0.06)
            self.element_appear(locate_type, locator_expression, timeout)
            element.clear()
            self.append_return(driver, fill_value, element)
        except Exception:
            raise Exception("元素填值失败")
        return True

    def element_screenshot(self, driver, locate_type, locator_expression):
        """
        元素截图
        :param driver:
        :param locate_type:
        :param locator_expression:
        :return:
        """
        ele_name = datetime.datetime.now().strftime("%Y-%m-%d:%H-%M-%s") + ".png"
        ele_img_dir_path = get_img_path(ele_name, True, ["web", "screenshot"])
        if not os.path.exists(ele_img_dir_path):
            os.makedirs(ele_img_dir_path)
        ele_path = ele_img_dir_path + ele_name
        self.find(driver, locate_type,locator_expression).screenshot(ele_path)
        return ele_path





