"""
@ Title:
@ Author: Cathy
@ Time: 2024/5/9 16:20
"""
def reverse(old_str):
    return old_str[::-1]

def reverse2(old_str):
    re_str = ''
    l = len(old_str) - 1
    while l >= 0:
        re_str += old_str[l]
        l -= 1
    return re_str

# 递归
def reverse3(old_str):
    l = len(old_str)
    if l > 0:
        reverse3(old_str[1:])
    print(''.join(old_str[-1]))


if __name__ == '__main__':
    s = 'abcdefg'
    reverse3(s)