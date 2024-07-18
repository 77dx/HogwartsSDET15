"""
@ Title:
@ Author: Cathy
@ Time: 2024/3/19 16:06
"""
'''
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
示例 1：
输入：nums = [3,2,3]
输出：3

示例 2：
输入：nums = [1,2,2,1,1,1,2,2]
输出：2
'''
def majorityElement(nums):
    l = len(nums)
    length_list = []
    for i in range(l):
        current_length = 1
        for j in range(i+1,l):
            if nums[i] == nums[j]:
                current_length += 1
        length_list.append(current_length)












if __name__ == '__main__':
    nums = [6,6,6,7,7]
    majorityElement(nums)