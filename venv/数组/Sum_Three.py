# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 3:25 下午
# @Author  : Estelle
# @File    : Sum_Three$.py

'''
https://leetcode-cn.com/problems/3sum/submissions/
'''

# 第一步: 遍历 所有的相邻两项的和
# 第二步：提取 同时要保证a,b,c是三个数，且不重复
# 复杂度太高


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return
        res = []
        setres = []
        for i, val in enumerate(nums):
            for j in range(i + 1, len(nums) - 1):
                b = -val - nums[j]
                if b in nums[j + 1:]:
                    temp = [val, nums[j], b]
                    setemp = set(sorted(temp))
                    if setemp in setres:
                        continue
                    else:
                        setres.append(setemp)
                        res.append(temp)

        return res



# 复杂度O(n2)
# 双指针左右下标 【必须要排序】

    def threeSum1(self, nums):
        n=len(nums)
        if(not nums or n<3):
            return []
        nums.sort()
        res=[]
        for i in range(n):
            if(nums[i]>0):
                return res
            if(i>0 and nums[i]==nums[i-1]):
                continue
            L=i+1
            R=n-1
            while(L<R):
                if(nums[i]+nums[L]+nums[R]==0):
                    res.append([nums[i],nums[L],nums[R]])
                    while(L<R and nums[L]==nums[L+1]):
                        L=L+1
                    while(L<R and nums[R]==nums[R-1]):
                        R=R-1
                    L=L+1
                    R=R-1
                elif(nums[i]+nums[L]+nums[R]>0):
                    R=R-1
                else:
                    L=L+1
        return res