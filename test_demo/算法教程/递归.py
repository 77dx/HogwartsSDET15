"""
@ Title:
@ Author: Cathy
@ Time: 2024/3/12 20:28
"""
# 用递归打印1-100
# 还没有理解递归的实现思路
def recoursion(n):
    if n <= 100:
        print(f"{n} ")
        recoursion(n + 1)



# 递归累加1-100  1+2+3+4+5....+100
def recoursion2(n):
    if n < 100:
        return n + recoursion2(n+1)
    else:
        return n


# 斐波那契数列是指这样一个数列：1，1，2，3，5，8，13，21，34，55，89……这个数列从第3项开始 ，每一项都等于前两项之和。
# 递归版
def fei(n):
    if n <=2:
        return 1
    return fei(n-2) + fei(n-1)

# 非递归版
def fei_n(n):
    if n <= 2:
        return 1
    a = 1
    b = 1
    res = 2
    for i in range(3, n+1):
        res = a + b
        a = b
        b = res
    return res

# 爬台阶问题
class DFS:
    res = 0
    n = 5
    def dfs(self,u):
        if u == self.n:
          self.res += 1
        if u < self.n:
            self.dfs(u+1)
            self.dfs(u+2)
        return self.res

# 全排列问题：给定一个不含重复数字的数组，返回其可能的全排列，你可以按任意顺序返回答案
# 输入： nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# 我的答案，没有实现回溯，只实现了一层排序
def all_f(nums):
    l = len(nums)
    res = []
    if l <= 1:
        return nums
    else:
        for i in range(0,l):
            s = []
            s.append(nums[i])
            for j in range(0,l):
                if j != i:
                    s.append(nums[j])
            res.append(s)
    print(res)

# leetcode的答案
def permutations(nums):
    if len(nums) <= 1:
        return nums
    else:
        n = len(nums)
        res = []
        def backtrack(first = 0):
            if first == n:
                res.append(nums)
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
        backtrack()
        return res







if __name__ == '__main__':
    nums = [1,2,3]
    print(permutations(nums))