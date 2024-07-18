"""
@ Title:
@ Author: Cathy
@ Time: 2024/4/19 17:41
"""


def levelOrder(node):
    res = []
    if not node:
        return res

    queue = []
    stack = []

    queue.append(node)

    while queue:
        r = []
        if not stack:
            node = queue.pop(0)
            stack.append(node)
        node = stack.pop()
        r.append(node.val)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)

        res.append(r)











