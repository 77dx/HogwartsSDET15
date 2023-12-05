import os

import yaml


class Base:

    base_url = 'https://www.baidu.com'

    def add(self):
        print('父类的加法')


class Son(Base):
    base_url = 'lllll'

    def get_base(self):
        print(self.base_url)



# Son().get_base()

# Deco和Deco2的区别？？？？？？？？？？？？？？？？
class Deco:

    def __call__(self, func):
        self.func = func
        # print(f"打印的是self.wrapper:{self.wrapper}")
        return self.wrapper

    def wrapper(self, *args, **kwargs):
        print("装饰器功能实现了")
        f = self.func(*args, **kwargs)
        print(f"打印的是f:{f}")
        return f

class Deco2:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print('加装的内容')
            return func(*args, **kwargs)
        return wrapper


class w:
    @Deco()
    def login(self, username, password):
        if username == "cathy" and password == '123456':
            print('登陆成功')
        else:
            print('登陆失败')

# m = w()
# m.login("111","333")


def hi(func, name="yasoob"):
    print("now you are inside the hi() function")


    def greet(name):
        return f"now you are in the greet() function:{name}"


    def welcome(usr):
        return f"now you are in the welcome() function:{usr}"

    if name  == "yasoob":
        return greet
    else:
        return welcome

def something():
    print('something done')

# hi(something())





root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(root_dir)
file_path = os.path.join(root_dir, 'web/resource/img/aa.jpeg')
# print(file_path)
f = root_dir + '/web/resource/img/aa.jpeg'
# print(f)
import pyautogui as ui

# ui.write(f)
# ui.typewrite("hello")
# ui.getActiveWindow()




def parse(fileName, steps):
    with open("../web/data_yaml/" + fileName, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    steps = data[steps]
    print(steps)
    print('********************')
    for step in steps:
        print(step['locator'])
    #     print(step['action'])
    #     print(step['gotoPage'])


# parse("main_page.yaml","order_list")


# import importlib
#
# module = importlib.import_module(name=".pub_order_page",package="web.web_page")
# print(module.__dir__()[-1])

# print(module.PubOrderPage().name)
# print(module.Demo().display_data())

import random

# print(random.randint(1,99))
# import sys
# print(sys.argv)
#
# import argparse
# print(argparse)


list_num = [1,2,3,4,5]
# print(max(list_num))
if not list_num:
    print(list_num)
