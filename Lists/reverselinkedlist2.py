"""
https://leetcode.com/problems/reverse-linked-list-ii/#/description

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        current = head
        prevNode = None
        index = 1
        while index < m:
            prevNode = current
            current = current.next
            index += 1
        nextNode = current.next
        while index < n:
            current.next = prevNode
            prevNode = current
            nextNode = nextNode.next
            index += 1
        return head if head.next else current