"""
@ Title:
@ Author: Cathy
@ Time: 2024/5/11 13:41
"""

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        return None



if __name__ == '__main__':
    print(fibonacci(10))
