"""
@ Title:
@ Author: Cathy
@ Time: 2024/5/28 20:01
"""
# 转字符串的方法
def isPalindrome(x):
    s = ''
    r = x
    if x < 0:
        return False
    elif x == 0:
        return True
    else:
        while x > 0:
            y = x % 10
            s = s + str(y)
            x = x // 10

        if r == int(s):
            return True
        else:
            return False

# 转列表的方法
def isPalindrome2(x):
    if x < 0:
        return False
    elif x == 0:
        return True
    else:
        n = []
        while x > 0:
            n.append(x % 10)
            x = x // 10
        re_n = n[::-1]
        if n == re_n:
            return True
        else:
            return False

# 需要学会将一个数字逆转后还是一个数字，我的计算方法非常的常规，并且在程序中无法实现，
# 假如为123，逆转后为321，我想的计算方法为：3*10*10+2*10+1，这个在程序中没有找到
# 可以实现的方法，看了答案，才知道，计算方法可以是这样的：3，(3*10+2)*10+1 = 321,好厉害！
def isPalindrome3(x):
    num = x
    if x < 0:
        return False
    elif x == 0:
        return True
    else:
        cur = 0
        while x > 0:
            cur = cur * 10 + x % 10
            x = x // 10
        if num == cur:
            return True
        else:
            return False




if __name__ == '__main__':

    print(isPalindrome3(99999))