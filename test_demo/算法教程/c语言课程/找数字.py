"""
@ Title:
@ Author: Cathy
@ Time: 2024/4/19 14:14
"""

# 函数的参数，列表，函数内列表内存地址与原列表一致，说明，入参时把列表和列表所有元素的引用都传递过来了。
# 在函数内修改列表的值，原列表的值也会被修改。
# c语言中，函数的入参是数组的话，传过来的只是实参数组的首元素的地址，所以，在函数内无法获得数组的长度，但是可以
# 获取到所有的数组元素。
def binary_search(list, n):

    for i,k in enumerate(list):
        if k == n:
            return i
    return -1


if __name__ == '__main__':
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    r = binary_search(list, 9)
    if r != -1:
        print(r)
    else:
        print("没有找到该数字")

