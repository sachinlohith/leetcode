"""
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/


Given a binary tree, return the bottom-up level order traversal of its nodes'
values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        queue = [(root, 0)]
        while queue:
            node, level = queue.pop(0)
            if node is not None:
                if level >= len(result):
                    result.append([])
                result[level] += [node.val]
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
        return result[::-1]
