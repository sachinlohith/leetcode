"""
https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/


You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].
"""


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        class Node:
            def __init__(self, v, s):
                self.val = v
                self.sum = s
                self.dup = 1
                self.left = None
                self.right = None

        def insert(num, node, ans, i, presum):
            if node is None:
                node = Node(num, 0)
                ans[i] = presum
            elif node.val == num:
                node.dup += 1
                ans[i] = presum + node.sum
            elif node.val > num:
                node.sum += 1
                node.left = insert(num, node.left, ans, i, presum)
            else:
                node.right = insert(num, node.right, ans, i, presum + node.dup + node.sum)
            return node

        ans = [0] * len(nums)
        root = None
        idx = len(nums) - 1
        while idx >= 0:
            root = insert(nums[idx], root, ans, idx, 0)
            idx -= 1
        return ans
