"""
@ Title:
@ Author: Cathy
@ Time: 2024/6/21 14:12
"""

def isValid(s: str):
    # 先用栈的方式解决试试
    list_s = list(s)
    stack = []
    while list_s:
        if stack:
            ret = list_s.pop()
            if stack[-1] == ")" and ret == "(":
                stack.pop()
            elif stack[-1] == "}" and ret == "{":
                stack.pop()
            elif stack[-1] == "]" and ret == "[":
                stack.pop()
            else:
                stack.append(ret)
        else:
            stack.append(list_s.pop())

    if stack:
        return False
    return True













if __name__ == '__main__':
    s = '{[]}'
    s2 = '(){}[]'
    print(isValid(s2))