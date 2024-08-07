"""
@ Title:
@ Author: Cathy
@ Time: 2024/3/19 13:42
"""
'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]

'''
class Solution:
    def twoSum(self, nums, target):
        two = []
        l = len(nums)
        for i in range(l):
            m = target - nums[i]
            for j in range(l):
                if i != j:
                    if nums[j] == m:
                        if i not in two and j not in two:
                            two.append(i)
                            two.append(j)
        print(two)

# 官方答案
class Solution2:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

def twoSum(nums,target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []




if __name__ == '__main__':
    nums = [-1,-2,-3,-4,-5]
    target = -8
    # print(Solution2().twoSum(nums, target))
    print(twoSum(nums, target))