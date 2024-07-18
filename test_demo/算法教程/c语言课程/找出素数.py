"""
@ Title:
@ Author: Cathy
@ Time: 2024/4/19 13:05
"""
import math


# 能被一个数整除的所有数里，除了本身，最大的被除数不会大于本身的开方，作为本次循环最大的优化点
def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False

    return True

# 这种写法更优，循环次数未增加，作为循环的开方值更具实际意义。
def is_prime2(n):
    i = 2
    while i <= int(math.sqrt(n)):
        if n % i == 0:
            return False
        i += 1

    return True





if __name__ == '__main__':
    n = 100
    count = 0
    while n <= 200:
        if is_prime2(n):
            count += 1
            print(n, end=' ')
        n += 1
    print(count)
