"""
https://leetcode.com/problems/reverse-linked-list/discuss/

Reverse a singly linked list.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


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
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

    def reverseListRec(self, head):
        def _reverse(node, prev=None):
            if not node:
                return prev
            n = node.next
            node.next = prev
            return self._reverse(n, node)
        return _reverse(head)
