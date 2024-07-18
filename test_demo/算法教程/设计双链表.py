"""
@ Title:
@ Author: Cathy
@ Time: 2024/4/6 18:35
"""

# leetcode提交未成功，有用例报错！！！

class Node:
    def __init__(self,val):
        self.prev = None
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    # 查找节点的值
    def get(self,index):
        if index < 0 or index >= self.size:
            return -1

        dummpy = self.getNode(index)
        return dummpy.val

    def getNode(self,index):
        if index < self.size // 2:
            p = self.head
            for _ in range(index+1):
                p = p.next
        else:
            p = self.tail
            for _ in range(self.size-index):
                p = p.prev
        return p

    def addAtIndex(self, index, val):
        if index > self.size:
            return
        if index < 0:
            index = 0

        new_node = Node(val)
        second = self.getNode(index)
        # 增加头节点
        if index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        # 增加尾节点
        elif index == self.size:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        # 增加中间节点
        else:
            new_node.next = second
            second.prev = new_node
            second.prev.next = new_node
            new_node.prev = second.prev

        self.size += 1

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        self.addAtIndex(self.size, val)

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return

        del_node = self.getNode(index)
        del_node.prev.next = del_node.next
        del_node.next.prev = del_node.prev

        self.size -= 1


