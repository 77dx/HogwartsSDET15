"""
@ Title:
@ Author: Cathy
@ Time: 2024/5/21 16:24
"""

class Solution:
    def aInB(self, a, b):
        for i in a:
            if i not in b:
                return False
        return True


    def minWindow(self, s: str, t: str) -> str:
        l = len(s)
        f_list = []
        if len(s) < len(t):
            return ""
        if s == t:
            return t
        if t in s:
            return t
        for t_ in t:
            for i in range(l):
                if t_ == s[i]:
                    f_list.append(s[i:])
        print(f_list)
        if not f_list:
            return ""
        else:
            s_list = []
            for f_ in f_list:
                if self.aInB(t, f_):
                    s_list.append(f_)
            if len(s_list) == 1:
                return s_list[0]
            for i in range(len(s_list) - 1):
                if len(s_list[i]) < len(s_list[i + 1]):
                    s_list[i], s_list[i + 1] = s_list[i + 1], s_list[i]
            return s_list[-1]


if __name__ == '__main__':
    # s = "ADOBECODEBANC"
    # t = "ABC"
    # s = "a"
    # t = "aa"
    # s = "a"
    # t = "a"
    s = "bbaac"
    t = "aba"
    c = Solution().minWindow(s, t)
    print(c)

    # print(first())
    # li = ['ADOBECODEBANC', 'BECODEBANC', 'BANC', 'CODEBANC']
    # for i in range(len(li)-1):
    #     if len(li[i]) < len(li[i+1]):
    #         li[i],li[i+1] = li[i+1],li[i]
    # print(li)





