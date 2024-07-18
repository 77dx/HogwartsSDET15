"""
@ Title:
@ Author: Cathy
@ Time: 2024/4/12 15:49
"""


class Deque:

    def __init__(self):
        self.list_ = []

    # 从队列的左侧入队
    def push_left(self, val):
        self.list_.insert(0, val)

    # 从队列的右侧入队
    def push_right(self, val):
        self.list_.append(val)

    # 从队列的左侧取出数据
    def get_left(self):
        return self.list_[0]
        # return self.list_.pop(0)

    # 从队列的右侧取出数据
    def get_right(self):
        return self.list_[-1]
        # return self.list_.pop()

    # 判断队列是否为空
    def is_empty(self):
        return True if not self.list_ else False

    # 统计队列元素的个数
    def size(self):
        return len(self.list_)


if __name__ == '__main__':
    d = Deque()
    print(d.is_empty())
    d.push_right(2)
    d.push_left(1)
    print(d.get_left())
    print(d.get_right())
    print(d.list_)
    print(d.size())