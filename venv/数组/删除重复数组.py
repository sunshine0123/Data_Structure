# -*- coding: utf-8 -*-
# @Time    : 2020/2/22 12:41 下午
# @Author  : Estelle
# @File    : 删除重复数组$.py


'''
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/solution/
'''
class Solution(object):

    ## 控制变化的变量
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums :
            return
        i ,n = 0, len(nums)
        while i < n-1:
            if nums[i]==nums[i+1]:
                nums.remove(nums[i]) ### remove操作是O(N)
                n = len(nums)
            else:
                i+=1
        return len(nums)

    ## 快慢指针

    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        i, j = 0, 1
        while j < len(nums):
            if nums[i] != nums[j]:
                nums[i + 1] = nums[j]
                j = j + 1
                i = i + 1
            else:
                j = j + 1

        return i + 1