"""
@ Title:
@ Author: Cathy
@ Time: 2024/6/21 20:12
"""

def minWindow(s: str, t: str) -> str:
    if s == t:
        return s
    if len(s) < len(t):
        return ""

    i = 0
    tmp = []
    list_t = list(t)
    while i < len(s):
        j = 0
        while j < len(t):
            if s[i] == t[j]:
                if list_t:
                    list_t.pop(j)
                    tmp.append(i)
            j += 1
        i += 1
    print(tmp)











if __name__ == '__main__':
        # s = "ADOBECODEBANC"
        # t = "ABC"
        # s = "a"
        # t = "aa"
        # s = "a"
        # t = "a"
        s = "bbaac"
        t = "aba"
        minWindow(s, t)

