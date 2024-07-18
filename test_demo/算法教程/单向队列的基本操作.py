"""
@ Title:
@ Author: Cathy
@ Time: 2024/4/12 15:34
"""
# python list，pop入参为下标；remove入参为value
class Queue:

    def __init__(self):
        self.list_ = []

    # 入队
    def push(self, val):
        self.list_.append(val)

    # 取出队头元素
    def front(self):
        if not self.is_empty():
            return self.list_[0]
        else:
            return None

    # 从队列中弹出队头元素
    def pop(self):
        self.list_.pop(0)

    # 判断队列是否为空
    def is_empty(self):
        return True if not self.list_ else False

    # 统计队列尺寸
    def size(self):
        return len(self.list_)


if __name__ == '__main__':
    # q = Queue()
    # q.push(4)
    # q.push(7)
    # q.push(10)
    # print(q.size())
    # print(q.front())
    # q.pop()
    # print(q.list_)

    list = [1,4,7,90,30]
    list.pop(2)
    print(list)
