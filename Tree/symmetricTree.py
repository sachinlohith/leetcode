"""
https://leetcode.com/problems/symmetric-tree/description/

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def traverse(left, right):
            if not left and not right:
                return True
            if left and right and left.val == right.val:
                return traverse(left.left, right.right) and traverse(left.right, right.left)
            return False

        return traverse(root, root)

    def isSymmetricIter(self, root):
        queue = [root, root]
        while queue:
            right = queue.pop()
            left = queue.pop()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            queue += [left.left, right.right, left.right, right.left]
        return True
