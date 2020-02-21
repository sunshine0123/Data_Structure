# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 3:25 下午
# @Author  : Estelle
# @File    : Max_Area$.py

'''
https://leetcode-cn.com/problems/container-with-most-water/
'''
### 遍历 max_area = height*width 固定一个最大化另一个

class Solution:
    def Max_Area(self,nums):
        i , j =0,len(j)
        Area = 0
        while i < j :
            temp = (j-i)*min(nums[i],nums[j])
            Area = max(Area,temp)
            if nums[i]<nums[j]:
                i+=1
            else:
                j-=1
        return Area