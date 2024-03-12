"""
@ Title:
@ Author: Cathy
@ Time: 2024/3/12 20:31
"""
'''读计算机组成原理，第一章有一个算法，用python试一下
   找出一组数字中，连续数字相同最长的字串;
   找出最长的字串，需要计算连续数字相同的长度，找出长度最长的那个序列
'''
def findMax():
    s = '23277366664792221'
    l = len(s)
    current_run_length = 1
    max_run_value = 0
    for i in range(0, l-1):
        if s[i] == s[i+1]:
            current_run_length += 1
        else:
            current_run_length = 1

        if current_run_length > max_run_value:
            max_run_value = current_run_length
    print(max_run_value)
