"""
@ Title:
@ Author: Cathy
@ Time: 2024/5/9 17:09
"""

def fun( n ):
    if n > 9:
        return fun(n // 10) + n % 10
    else:
        return n


if __name__ == '__main__':
    n = 1729
    print(fun(n))

