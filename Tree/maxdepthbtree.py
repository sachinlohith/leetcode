"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        visited = collections.deque([root])
        nextVisited = collections.deque([])
        length = 0
        while visited:
            length += 1
            while visited:
                nextNode = visited.popleft()
                if nextNode.left:
                    nextVisited.append(nextNode.left)
                if nextNode.right:
                    nextVisited.append(nextNode.right)
            visited = nextVisited
            nextVisited = collections.deque([])
        return length
