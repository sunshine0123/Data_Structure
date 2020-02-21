# -*- coding: utf-8 -*-
# @Time    : 2020/2/21 11:50 上午
# @Author  : Estelle
# @File    : climb_stars$.py

## f(5) = F(4)+F(3)
## f(4) = f(3)+f(2)
## f(3) = f(2)+f(1)
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        if n==2:
            return 2
        if n ==1:
            return 1
        if n>2:
            res = [0]*n
            res[0:2] =[1,2]
            j = 2
            while j<n:
                res[j] = res[j-1]+res[j-2]
                j = j+1
            return res[-1]
