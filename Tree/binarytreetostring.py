"""
https://leetcode.com/problems/construct-string-from-binary-tree/#/description
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    result = ""

    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def preOrder(t):
            self.result += "("
            if t:
                self.result += str(t.val)
                if t.left:
                    preOrder(t.left)
                if not t.left and t.right:
                    self.result += "()"
                if t.right:
                    preOrder(t.right)
            self.result += ")"
        preOrder(t)
        return self.result[1:-1]
