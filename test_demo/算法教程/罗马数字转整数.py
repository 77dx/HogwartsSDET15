"""
@ Title:
@ Author: Cathy
@ Time: 2024/5/29 17:36
"""

def romanToInt(s):
    romanDic = {
        "I": 1, "II": 2, "III": 3, "a": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "b": 9, "X": 10,
        "c": 40, "L": 50, "d": 90, "C": 100, "e": 400, "D": 500, "f": 900, "M": 1000
    }
    s = s.replace("IV", "a")
    s = s.replace("IX", "b")
    s = s.replace("XL", "c")
    s = s.replace("XC", "d")
    s = s.replace("CD", "e")
    s = s.replace("CM", "f")

    n = 0
    for i in s:
        if i in romanDic.keys():
            n += romanDic[i]

    return n

# 参考了答案，看结论才知道，左边的数比右边的数值小时，就减去左边的数，这才是核心啊，能总结出来其中的数学规律真的很重要。
def romanToInt2(s):
    romanDic = {
        "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10,
        "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000
    }
    l = len(s)
    n = 0
    for i in range(l):
        if i < l - 1:
            if romanDic[s[i]] < romanDic[s[i+1]]:
                n -= romanDic[s[i]]
            else:
                n += romanDic[s[i]]
        else:
            n += romanDic[s[i]]

    return n





if __name__ == '__main__':
    print(romanToInt2("IX"))
