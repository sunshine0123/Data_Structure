# -*- coding: utf-8 -*-
# @Time    : 2020/2/21 4:23 下午
# @Author  : Estelle
# @File    : inked-list-cycle$.py

'''
https://leetcode-cn.com/problems/linked-list-cycle/
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):


    ##删除掉不直接的步骤是环总是环
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        anas = head
        while anas.next.next:
            if anas != anas.next.next:
                anas.next = anas.next.next
                anas = anas.next
                if anas is None or anas.next is None:
                    return False
                    break
            else:
                return True
                break

        return False

# 快慢指针
   def hasCycle(self,head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        cur = head
        pre = head.next
        while pre.next and pre.next.next:
            if cur != pre:
                cur = cur.next
                pre = pre.next.next
            else:
                return True

        return False