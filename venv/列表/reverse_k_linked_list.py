# -*- coding: utf-8 -*-
# @Time    : 2020/2/22 12:40 下午
# @Author  : Estelle
# @File    : reverse_k_linked_list$.py

'''
https://leetcode-cn.com/problems/reverse-nodes-in-k-group/submissions/
'''
class Solution:

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Dummy node initialization
        dummy = jump = ListNode(-1)
        dummy.next = l = r = head

        while True:
            count = 0
            while r and count < k:
                count += 1
                r = r.next
            if count == k:
                pre, cur = r, l
                for _ in range(k):
                    temp = cur.next
                    cur.next = pre
                    pre = cur
                    cur = temp
                jump.next = pre
                jump = l
                l = r
            else:
                return dummy.next