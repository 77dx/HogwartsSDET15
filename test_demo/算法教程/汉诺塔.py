"""
@ Title:
@ Author: Cathy
@ Time: 2024/4/28 17:25
"""
# 将a全部放到c中，就很牛，不是特别理解

def hanota(a, b, c):
    n = len(a)
    move(n, a, b, c)


def move(n, a, b, c):
    if n == 1:
        c.append(a[-1])
        a.pop()
    else:
        move(n-1, a, c, b)
        c.append(a[-1])
        a.pop()
        move(n-1, b, a, c)
    return c









if __name__ == '__main__':
    a = [2, 1, 0]
    b = []
    c = []
    print(hanota(a, b, c))
