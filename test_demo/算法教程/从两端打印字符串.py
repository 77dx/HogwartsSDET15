"""
@ Title:
@ Author: Cathy
@ Time: 2024/4/12 16:30
"""
"""
welcome to C!!!
w.............!
we...........!!
wel.........!!!
"""

def deque():
    s1 = list('welcome come to Shenzhen!!!')
    s2 = list('*' * len(s1))
    left = 0
    right = len(s1) - 1
    while left <= right:
        s2[left] = s1[left]
        s2[right] = s1[right]
        left += 1
        right -= 1
        print(''.join(s2))

if __name__ == '__main__':
    deque()

