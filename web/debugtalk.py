from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep, time
from functools import wraps


'''
 处理弹窗装饰器，
 在登录进入主页后，可能会有多个活动弹窗出现，由于操作速度过快，弹窗可能会在点击操作之后在其他页面弹出，所以在需要的地方可加上装饰器
 处理弹窗
 '''
class DecoPopAd:
    def __init__(self, driver):
        self.driver = driver

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                ele_ad = self.driver.find_element(By.XPATH, '//*[@class="close-icon"]')
                if ele_ad:
                    ele_ad.click()
            except Exception as e:
                print(f"页面未出现弹窗广告{e}")
            finally:
                return func(*args, **kwargs)
        return wrapper


# 单例模式
def singleton(cls, *args, **kwargs):
    instance = {}
    def _singleton():
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return _singleton