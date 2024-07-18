"""
@ Title:
@ Author: Cathy
@ Time: 2024/4/10 18:55
"""

"""
在一个连续增加或者减小的数组中查找某一个元素，使用二分法，
重点是判断循环结束条件！
"""
def division():
    list = [1, 2, 7, 40, 59, 61, 73, 88, 92]
    k = 92   # 要查找的数
    left = 0  # 左边下标
    right = len(list) - 1  # 右边的下标
    while left <= right:  # 左右两边的下标没有交叉，说明二分法还没结束，还有区间可二分
        mid = (left + right) // 2   # //代表整数相除，/代表浮点数相除
        if list[mid] < k:    # 目标值比中间值大，说明区间在右边，left调整
            left = mid + 1
        elif list[mid] > k:  # 目标值在左边，right调整
            right = mid - 1
        else:
            print(mid)    # 目标值于num[mid]相等，说明找到元素了，返回下标
            break
    if left > right:   # 左右下标已交叉，说明无区间可继续二分，未找到目标值
        print("sorry...")

division()