"""
@ Title:
@ Author: Cathy
@ Time: 2024/4/10 18:43
"""


"""
第一版写的是双层循环，忽略了阶乘的连续性，下一个数的阶乘是在上一个数阶乘的基础上乘以这个数，
这样的话，前面阶乘的部分是可以复用的。代码执行效率更高，更加简洁。
"""
# 计算 1！+ 2！+3！+... +n!
def factorial_sum(n: int):
    sum = 0
    ret = 1
    for i in range(1, n+1):
        ret = ret * i
        sum += ret
    print(sum)


factorial_sum(3)