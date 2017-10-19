class solution:
    def longestConsequitive(self, root):
        if root is None:
            return 0
        from collections import deque
        queue = deque([(root, 1)])
        maxVal = 1
        while queue:
            node, size = queue.popleft()
            if node.left is not None:
                if node.left.val - node.val == 1:
                    leftSize = size + 1
                    maxVal = max(maxVal, leftSize)
                else:
                    leftSize = 1
                queue.append((node.left, leftSize))
            if node.right is not None:
                if node.right.val - node.val == 1:
                    rightSize = size + 1
                    maxVal = max(maxVal, rightSize)
                else:
                    rightSize = 1
                queue.append((node.right, rightSize))
        return maxVal

    def longestConsequitiveRec(self, root):
        self.maxVal = 0
        def helper(root):
            if root is None:
                return 0
            l = helper(root.left)
            r = helper(root.right)

            if root.left is not None and root.left.val - root.val == 1:
                fromLeft = l + 1
            else:
                fromLeft = 1
            if root.right is not None and root.right.val - root.val == 1:
                fromRight = r + 1
            else:
                fromRight = 1
            self.maxVal = max(self.maxVal, fromLeft, fromRight)
            return max(fromRight, fromRight)
