# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        result = []
        def printLevel(root, level):
            if not root:
                return
            if level == 1:
                result[-1].append(root.val)
            else:
                printLevel(root.left, level-1)
                printLevel(root.right, level-1)
        def height(root):
            if not root:
                return 0
            else:
                lh = height(root.left)
                rh = height(root.right)
                if lh < rh:
                    return rh + 1
                else:
                    return lh + 1
        for i in xrange(1, height(root)+1):
            result.append([])
            printLevel(root, i)
        return map(lambda x: sum(x)/(len(x) + 0.0), result)

    def optimalAverageOfLevels(self, root):
        info = []

        def dfs(node, depth=0):
            if node:
                if len(info) <= depth:
                    info.append([0, 0])
                info[depth][0] += node.val
                info[depth][1] += 1
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
        dfs(root)

        return [s/float(c) for s, c in info]
