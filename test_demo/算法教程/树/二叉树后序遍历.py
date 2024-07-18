"""
@ Title:
@ Author: Cathy
@ Time: 2024/4/19 17:25
"""

# 一点也没懂。。。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def postorderTraversal(self, root):
        res = list()
        if not root:
            return res
        node = root
        stack = []
        prev = None

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if not node.rignt or root.right == prev:
                res.append(node.val)
                prev = node
                node = None
            else:
                stack.append(node)
                node = node.right
        return res
