"""
https://leetcode.com/problems/subtree-of-another-tree/description/


Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
            O(|s| * |t|)
        """
        def traverse(s, t):
            def equals(s, t):
                if (not s) and (not t):
                    return True
                if (not s) or (not t):
                    return False
                return s.val == t.val and equals(s.left, t.left) and equals(s.right, t.right)
            return (s is not None) and (equals(s, t) or traverse(s.left, t) or traverse(s.right, t))
        return traverse(s, t)

    def isSubtreeOpt(self, s, t):
        """
            O(|s| + |t|)
        """
        from hashlib import sha256
        def hash_(x):
            S = sha256()
            S.update(x)
            return S.hexdigest()

        def merkle(node):
            if not node:
                return '#'
            m_left = merkle(node.left)
            m_right = merkle(node.right)
            node.merkle = hash_(m_left + str(node.val) + m_right)
            return node.merkle

        merkle(s)
        merkle(t)
        def dfs(node):
            if not node:
                return False
            return (node.merkle == t.merkle or
                    dfs(node.left) or dfs(node.right))

        return dfs(s)
