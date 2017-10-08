# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = []

        def tilt(root):
            if not root:
                return 0
            ltilt = tilt(root.left)
            rtilt = tilt(root.right)
            result.append(abs(ltilt - rtilt))
            return root.val + ltilt + rtilt
        tilt(root)
        return sum(result)
