# -*- coding: utf-8 -*-
# @Time    : 2020/2/21 12:10 下午
# @Author  : Estelle
# @File    : everse-linked-list$.py


'''
https://leetcode-cn.com/problems/reverse-linked-list/submissions/
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        cur = head
        val = []
        while cur:
            val.append(cur.val)
            cur = cur.next
        val = val[::-1]
        i = 1
        res = ListNode(val[0])
        cur = res
        while i <len(val):
            cur.next = ListNode(val[i])
            cur = cur.next
            i +=1

        return res


## 双指针 ，一个指本身，一个指前身
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev


    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        change = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return change
