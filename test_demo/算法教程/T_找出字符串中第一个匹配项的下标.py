"""
@ Title:
@ Author: Cathy
@ Time: 2024/6/21 15:35
"""

def strStr(haystack: str, needle: str):
    h = len(haystack)
    n = len(needle)
    if needle in haystack:
       for i in range(h):
           if haystack[i] == needle[0]:
               if haystack[i:i+n] == needle:
                   return i
    else:
        return -1







if __name__ == '__main__':
    haystack = "sadbutsad"
    needle = "sad"
    # haystack = "leetcode"
    # needle = "leeto"
    print(strStr(haystack, needle))