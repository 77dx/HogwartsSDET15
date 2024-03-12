"""
@ Title:
@ Author: Cathy
@ Time: 2024/3/12 20:28
"""
# 用递归打印1-100
# 还没有理解递归的实现思路
def recoursion(n):
    if n <= 100:
        print(f"{n} ")
        recoursion(n + 1)



if __name__ == '__main__':
    recoursion(1)
