"""
https://leetcode.com/problems/sum-of-left-leaves/description/



Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        leaves = []
        def getLeaves(root):
            if not root:
                return
            if root.left:
                if not root.left.left and not root.left.right:
                    leaves.append(root.left.val)
                else:
                    getLeaves(root.left)
            getLeaves(root.right)
        getLeaves(root)
        return sum(leaves)

    def sumOfLeftLeavesOpt(self, root):
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return (self.sumOfLeftLeaves(root.left) +
                self.sumOfLeftLeaves(root.right))   # isn't leave