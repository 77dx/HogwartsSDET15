"""
@ Title:
@ Author: Cathy
@ Time: 2024/4/12 14:44
"""


class Stack:

    def __init__(self):
        self.list_ = []

    # 将元素压进栈中
    def push(self, val):
        self.list_.append(val)

    # 将元素弹栈
    def pop(self):
        self.list_.pop()

    # 判断栈是否为空，空返回true,非空返回false
    def is_empty(self):
        return not self.list_

    # 拿到栈顶元素
    def top(self):
        return self.list_[-1] if not self.is_empty() else None

    # 统计栈的大小
    def size(self):
        return len(self.list_)


if __name__ == '__main__':
    s = Stack()
    # print(s.size())
    s.push(2)
    s.push(3)
    # s.pop()
    # print(s.is_empty())
    s.push(5)
    print(s.size())
    print(s.list_)
