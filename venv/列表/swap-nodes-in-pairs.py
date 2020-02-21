# -*- coding: utf-8 -*-
# @Time    : 2020/2/21 2:02 下午
# @Author  : Estelle
# @File    : swap-nodes-in-pairs$.py

'''
https://leetcode-cn.com/problems/swap-nodes-in-pairs/
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## O(1) S(1)
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        while head and head.next:
            first = head
            second = head.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            head = prev.next

        return dummy.next


    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        P = self.swapPairs(head.next.next)
        t = head.next
        t.next = head
        head.next=P
        return t



# pre->a->b->b.next
# pre->b->a->b.next
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre,pre.next = self,head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next,b.next,a.next = b,a,b.next
            pre = a
        return self.next