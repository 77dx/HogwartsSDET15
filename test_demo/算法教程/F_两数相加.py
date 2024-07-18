"""
@ Title:
@ Author: Cathy
@ Time: 2024/6/20 16:43
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 用的是最常规的思路做的，最后一步也没实现，不会创建新的链表
class Solution:
    def create_linked_list(self, elements):
        head = None
        for element in elements:
            new_node = ListNode(element)
            if head is None:
                head = new_node
            else:
                cur = head
                while cur.next is not None:
                    cur = cur.next
                cur.next = new_node
        return head

    def addTwoNumbers(self, l1, l2):
        # 将链表的值取出来压栈
        list1 = []
        list2 = []
        # while l1:
        #     list1.append(l1.val)
        #     l1 = l1.next
        # while l2:
        #     list2.append(l1.val)
        #     l2 = l2.next
        for i, j in zip(l1, l2):
            list1.append(i)
            list2.append(j)

        # 将栈中的数字弹出来，计算为十进制数
        s1 = 0
        s2 = 0
        len1 = len(list1)
        len2 = len(list2)
        for m, n in zip(range(len1),range(len2)):
            if m < len1 - 1:
                s1 = (s1 + list1.pop()) * 10
            else:
                s1 = s1 + list1.pop()
            if n < len2 - 1:
                s2 = (s2 + list2.pop()) * 10
            else:
                s2 = s2 + list2.pop()

        # 相加两数
        s3 = s1 + s2

        # 将数字取出来
        list3 = []
        while s3 > 0:
            list3.append(s3 % 10)
            s3 = s3 // 10

        # 创建链表，把列表的值写入链表
        l3 = self.create_linked_list(list3)
        return l3


# 题解，还未理解，先这样吧
class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 创建一个结点值为 None 的头结点, dummy 和 p 指向头结点, dummy 用来最后返回, p 用来遍历
        dummy = p = ListNode()
        s = 0               # 初始化进位 s 为 0
        while l1 or l2 or s:
            # 如果 l1 或 l2 存在, 则取l1的值 + l2的值 + s(s初始为0, 如果下面有进位1, 下次加上)
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            p.next = ListNode(s % 10)       # p.next 指向新链表, 用来创建一个新的链表
            p = p.next                      # p 向后遍历
            s //= 10                        # 有进位情况则取模, eg. s = 18, 18 // 10 = 1
            l1 = l1.next if l1 else None    # 如果l1存在, 则向后遍历, 否则为 None
            l2 = l2.next if l2 else None    # 如果l2存在, 则向后遍历, 否则为 None
        return dummy.next   # 返回 dummy 的下一个节点, 因为 dummy 指向的是空的头结点, 下一个节点才是新建链表的后序节点






if __name__ == '__main__':
    s = Solution()
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    s.addTwoNumbers(l1, l2)
