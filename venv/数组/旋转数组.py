# -*- coding: utf-8 -*-
# @Time    : 2020/2/22 2:17 下午
# @Author  : Estelle
# @File    : 旋转数组$.py

'''
https://leetcode-cn.com/problems/rotate-array/discuss/?currentPage=1&orderBy=most_votes&query=
'''

#1 暴力方法

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            t = nums[-1]
            for j in range(len(nums)):
                temp =nums[j]
                nums[j]=t
                t = temp
        return nums

# 内部分开旋转【找规律】
    def rotate(self,nums,k):
        k %=len(nums)
        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,len(nums)-1)
        return nums

    def reverse(self,nums,start,end):
        while start <end:
            t = nums[start]
            nums[start] = nums[end]
            nums[end] = t
            start+=1
            end-=1