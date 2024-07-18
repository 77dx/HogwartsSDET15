"""
@ Title:
@ Author: Cathy
@ Time: 2024/4/17 17:37
"""

class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 前序遍历：根->左->右
# 迭代法，用栈实现，先从根节点开始遍历左节点，同时将左节点压栈，直到左节点为空后，开始弹栈(此时左侧的左节点遍历完毕)，
# 查询该节点的右节点，继续弹栈，直到弹出根节点，查出根节点的右节点不为空时，开始压栈右侧的左节点，直到左节点为空，开始弹栈，
# 查找右节点，直到栈为空，跳出循环
def preorderTraversal(root):
    res = list()
    if not root:
        return res

    stack = []
    node = root
    while stack or node:
        while node:
            res.append(node.val)
            stack.append(node)
            node = node.left
        node = stack.pop()
        node = node.right
    res = res.reverse()
    return res

# 递归法
def preorderTraversal2(root):

    def preorder(node):
        if not node:
            return
        res.append(node.val)
        preorder(node.left)
        preorder(node.right)

    res = list()
    node = root
    preorder(node)
    return res















