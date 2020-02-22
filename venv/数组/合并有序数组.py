# -*- coding: utf-8 -*-
# @Time    : 2020/2/22 9:11 下午
# @Author  : Estelle
# @File    : 合并有序数组$.py
'''

https://leetcode-cn.com/problems/merge-sorted-array/submissions/
'''



class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        cp = nums1[:m]
        i, j, k = 0, 0, 0
        while i < m and j < n:
            if cp[i] < nums2[j]:
                nums1[k] = cp[i]
                i += 1
                k += 1
            else:
                nums1[k] = nums2[j]
                j += 1
                k += 1
        if i < m:
            nums1[k:] = cp[i:]
        if j < n:
            nums1[k:] = nums2[j:]

        return nums1
