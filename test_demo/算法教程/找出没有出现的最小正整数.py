"""
@ Title:
@ Author: Cathy
@ Time: 2024/6/13 16:48
"""

def firstMissingPositive(nums):
    l = len(nums)
    x = [False] * (l+1)

    for i in nums:
        if i > 0 and i <= 1:
            x[i] = True

    for i in range(1, l+1):
        if not x[i]:
            return i

    return l+1







if __name__ == '__main__':
    nums1 = [1, 2, 0]
    nums2 = [3, 2, -1, 1]
    nums3 = [7, 8, 9, 11, 12]
    nums4 = [5, 2, 1]
    print(firstMissingPositive(nums4))