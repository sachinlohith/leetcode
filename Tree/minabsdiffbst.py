"""
https://leetcode.com/problems/minimum-absolute-difference-in-bst/#/description


Given a binary search tree with non-negative values, find-
the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which -
is the difference between 2 and 1 (or between 2 and 3).
Note: There are at least two nodes in this BST.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        diff = float("inf")
        if root is None:
            return diff
        if root.left:
            diff = min(diff, abs(root.val - root.left.val))
            right = root.left
            while right.right is not None:
                right = right.right
            diff = min(diff, abs(root.val - right.val))
        if root.right:
            diff = min(diff, abs(root.val - root.right.val))
            left = root.right
            while left.left is not None:
                left = left.left
            diff = min(diff, abs(root.val - left.val))
        return min(diff,
                   self.getMinimumDifference(root.left),
                   self.getMinimumDifference(root.right))

    def optimalGetMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        import sys
        self.lst = []
        self.inorder(root)
        mindiff = sys.maxint
        for i in range(1, len(self.lst)):
            mindiff = min(mindiff, self.lst[i] - self.lst[i - 1])
        return mindiff

    def inorder(self, root):
        if not root:
            return
        if root.left:
            self.inorder(root.left)
        self.lst.append(root.val)
        if root.right:
            self.inorder(root.right)
