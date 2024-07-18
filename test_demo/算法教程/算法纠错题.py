"""
@ Title:
@ Author: Cathy
@ Time: 2024/7/4 14:11
"""

# 原题目没有说是什么算法错了，就改成了我熟悉的冒泡排序了。
def selectSort(arr):

    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


if __name__ == '__main__':
    arr = [20, 40, 2, 7, 36, 77, 92]
    print(selectSort(arr))