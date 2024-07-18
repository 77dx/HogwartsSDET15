"""
@ Title:
@ Author: Cathy
@ Time: 2024/5/11 13:22
"""


def square(n, k):
    if k > 0:
        return n * square(n, k-1)
    elif k == 0:
        return 1


if __name__ == '__main__':
    n = -3
    k = 3

    print(square(n, k))
