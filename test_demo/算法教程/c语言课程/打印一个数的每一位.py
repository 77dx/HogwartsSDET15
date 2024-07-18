"""
@ Title:
@ Author: Cathy
@ Time: 2024/5/9 15:53
"""


def fun( n ):

    if n > 9:
        fun(n // 10)

    print(n % 10,end=' ')




if __name__ == '__main__':
    n = 1234
    fun(n)
