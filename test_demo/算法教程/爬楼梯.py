"""
@ Title:
@ Author: Cathy
@ Time: 2024/5/21 15:22
"""

# 在n=44时，递归会超时
def climbStairs(n):
    if n < 1:
        return
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return climbStairs(n-1)+climbStairs(n-2)


# leetcode上面优化后的代码,用循环实现的
def climbStairs2(n: int) -> int:
    f0 = f1 = 1
    for _ in range(2, n+1):
        f0, f1 = f1, f0+f1
    return f1





if __name__ == '__main__':
    n = 1
    print(climbStairs2(44))
