"""
@ Title:
@ Author: Cathy
@ Time: 2024/3/6 18:53
"""

# 一个下午没弄出来一个算法，自己写个之前会的，看看还记得不

# 比较简单，毫无成就感

def solution():
    for i in range(1,10):
        for j in range(1,i+1):
            r = j * i
            print(f"{j} * {i} = {r}\t", end="")
        print("\n")







if __name__ == '__main__':
    solution()

