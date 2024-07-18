"""
@ Title:
@ Author: Cathy
@ Time: 2024/4/19 13:46
"""

def is_leap_year(y):
    if y % 4 == 0 and y % 100 != 0:
        return 1
    elif y % 400 == 0:
        return 1
    return 0


if __name__ == '__main__':
    y = 1000
    count = 0
    while y <= 2000:
        if is_leap_year(y):
            print(y, end=' ')
            count += 1
        y += 1
    print('\n')
    print(count)