"""
@ Title:
@ Author: Cathy
@ Time: 2024/4/19 16:40
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    res = list()
    node = root

    stack = []
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        res.append(node.val)
        node = node.right

    return res



