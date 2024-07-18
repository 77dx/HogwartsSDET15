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
    pass

# 2,3,5,7,11,13,17,19,34
def get_sushu():
    r = []
    for i in range(2,101):
        if i == 2:
            r.append(i)
        else:
            if 0 not in [i%j for j in range(2,i)]:
                r.append(i)
    print(r)

# a=【‘aasc’，‘bszc’，‘ab’】找出里面有c的，都改成we
def change_str():

    a = ['aasc','bszc','ab']

    for i in range(0,len(a)):
        if 'c' in a[i]:
            print(id(a[i]))
            a[i] = a[i].replace('c','we')
            print(id(a[i]))

    print(a)

'''
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
'''
def merge(nums1, m, nums2, n):
    for i in range(m+n):
        for j in range(n):
            if nums2[j]>nums1[i] and nums2[j]==nums1[i+1]:
                nums1.insert(i+2,nums2[j])
            elif nums2[j]>nums1[i] and nums2[j]<nums1[i+1]:
                nums1.insert(i+1, nums2[j])
            elif i>=m and nums2[j]>=nums1[i]:
                nums1[i] = nums2[j]


    print(nums1)

'''
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
示例 1：
输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2]
解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。例如，函数返回的新长度为 2 ，而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。
示例 2：
输入：nums = [0,1,2,2,3,0,4,2], val = 2
输出：5, nums = [0,1,3,0,4]
解释：函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。注意这五个元素可为任意顺序。你不需要考虑数组中超出新长度后面的元素。
'''
def removeElement(nums, val: int) -> int:
    '''
    利用直接删除数组元素的方法行不通，一定会数组越界，因为在for循环时，数组的长度时固定的，即循环过程中数组实际长度变小，
    循环的长度还是原数据的长度，导致后面的取值越界。
    看了官方的答案一是数组元素替换的方法，设置两个指针，一个是去除数据后的指针left，另一个是循环数组的指针right，
    判断如果当前元素与比较数组不相同时，给left指针赋值，这样left的指针是连续的，且数据都是与比较数据不相同的，
    整个过程只是将元素交换位置，而最后几位数据还是原数据。
    但是过程中会有重复赋值的动作。
    :param nums:
    :param val:
    :return:
    '''
    left = 0
    for right in range(0, len(nums)):
        if nums[right] != val:
            nums[left] = nums[right]
            left += 1
    return left

def removeElement2(nums, val: int) -> int:
    '''
    第二种方法
    :param nums:
    :param val:
    :return:
    '''
    left = 0
    right = len(nums)
    while left < right:
        if nums[left] == val:
            nums[left] = nums[right-1]
            right -= 1
        else:
            left += 1
    print(left)



'''
合并两个有序数组
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
示例 1：

输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
示例 2：

输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
解释：需要合并 [1] 和 [] 。
合并结果是 [1] 。
示例 3：

输入：nums1 = [0], m = 0, nums2 = [1], n = 1
输出：[1]
解释：需要合并的数组是 [] 和 [1] 。
合并结果是 [1] 。
注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。
'''
def merge2(nums1, m: int, nums2, n: int) -> None:
    # i = m
    # j = 0
    # while i< m+n:
    #     if j < n:
    #         nums1[i] = nums2[j]
    #         i += 1
    #         j += 1
    # nums1.sort()
    # print(nums1)
    # nums1[m:] = nums2
    # nums1.sort()
    # print(nums1)
    pass

from time import sleep
from threading import Thread
class Thread_Test(Thread):

    def print_A(self):
        print("A")

    def print_B(self):
        print("B")

    def run(self):
        t1 = Thread(target=self.print_A)
        t2 = Thread(target=self.print_B)
        while True:
            t1.start()
            sleep(1)
            t2.start()




a = 20
class Test01:

    def printa(self):
        b = 30
        def printb():
            print(b)
        return printb()


def recursion(num):
    if num > 9:
        recursion(num // 10)
    print(num % 10)

# python的递归深度为998
def recursion2(n):
    if n < 998:
        recursion2(n + 1)


def str_len(s):
    print(s[:-1])

def bubble_sort():
    list_ = [9,8,7,6,5,4,3,2,1,0]
    l = len(list_)
    for i in range(l-1):
        for j in range(l-i-1):
            if list_[j]>list_[j+1]:
                list_[j],list_[j+1] = list_[j+1],list_[j]
    return list_







if __name__ == '__main__':
    # recursion2(1)
    # s = 'jane'
    # str_len(s)
    # n = False
    # if range(0):
    #     print(2)
    # s = 'hhhahhahah'
    # print(len(s))
    print(bubble_sort())













