# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 3:24 下午
# @Author  : Estelle
# @File    : Remove_Zeros$.py
# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 7:29 下午
# @Author  : Estelle
# @File    : 1_Array.py$.py
'''
1. prepend O(1)
2. append O(1)
3. lookup O(1)
4. insert O(n)
5. delect O(n)
'''

''' 
    移动零
    https://leetcode-cn.com/problems/move-zeroes/

'''


class Solution:
    '''
       双指针，一个只记录非零的索引，一个遍历
    '''


def move_zeros(self, nums):
    j = 0
    for i in range(0, len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            if i != j:
                nums[i] = 0
            j += 1

    return nums


'''
   交换
'''


def moveZeros1(self, nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
            j += 1
    return nums


'''
滚雪球
'''


def moveZeros2(self, nums):
    if len(nums) <= 1:
        return nums

    temps = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            temps += 1
        else:
            if i - temps >= 0:
                t = nums[i]
                nums[i] = 0
                nums[i - temps] = nums[i]

    return nums






