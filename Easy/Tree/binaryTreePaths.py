"""
https://leetcode.com/problems/binary-tree-paths/description/


Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        def traverse(root, path):
            if not root:
                return
            path = path + "->" + str(root.val) if path else str(root.val)
            if not root.left and not root.right:
                result.append(path)
                return
            if root.left:
                traverse(root.left, path)
            if root.right:
                traverse(root.right, path)
        traverse(root, "")
        return resul

    # dfs + stack
    def binaryTreePaths1(self, root):
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls + str(node.val))
            if node.right:
                stack.append((node.right, ls + str(node.val) + "->"))
            if node.left:
                stack.append((node.left, ls + str(node.val) + "->"))
        return res

    # bfs + queue
    def binaryTreePaths2(self, root):
        if not root:
            return []
        res, queue = [], collections.deque([(root, "")])
        while queue:
            node, ls = queue.popleft()
            if not node.left and not node.right:
                res.append(ls + str(node.val))
            if node.left:
                queue.append((node.left, ls + str(node.val) + "->"))
            if node.right:
                queue.append((node.right, ls + str(node.val) + "->"))
        return res

    # dfs recursively
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        self.dfs(root, "", res)
        return res

    def dfs(self, root, ls, res):
        if not root.left and not root.right:
            res.append(ls + str(root.val))
        if root.left:
            self.dfs(root.left, ls + str(root.val) + "->", res)
        if root.right:
            self.dfs(root.right, ls + str(root.val) + "->", res)