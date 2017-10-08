class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        def check(x, y):
            return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[x])

        def traverse(x, y):
            if not check(x, y):
                return 0
            if grid[x][y] == 0:
                return 0
            grid[x][y] = 0
            return 1 + traverse(x + 1, y) + traverse(x - 1, y) + traverse(x, y + 1) + traverse(x, y - 1)

        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                result = max(result, traverse(row, col))
        return result
