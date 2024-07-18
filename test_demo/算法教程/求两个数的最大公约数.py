"""
@ Title:
@ Author: Cathy
@ Time: 2024/4/16 18:13
"""

def sort_():
    list = [3,5,21,43,77,87,23]
    m = len(list)
    for i in range(m-1):
        for j in range(m-1-i):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    print(list)


def func():
    i = 3
    while i <= 100:
        if i % 3 == 0:
            print(i, end=' ')
        i += 3


# func()

# 求两个数的最大公约数
# 思路：两个数的最大公约数最大值为其中较小的那个值，那么先假设最大公约数是较小的那个值，
# 然后将这个值进行判断，是否可以同时被两个数整数，如不能就减一，再次循环判断，直到两个数
# 都可以被整除时跳出循环即可，因为是递减的，所以遇到的第一个能两数整数的即肯定是最大公约数。
def func2(m, n):
    if m < n:
        max = m
    else:
        max = n

    while True:
        if m % max == 0 and n % max == 0:
            print(f"最大公约数是{max}")
            break
        max -= 1


# func2(1,1)


# 求最大公约数，辗转相除法
def func3(m, n):
    while m % n:
        t = m % n
        m = n
        n = t
    print(n)

# func3(18, 9)

import math
print(math.sqrt(25))
