class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        def check(x, y):
            return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[x])

        self.shapes = []
        self.shape = []
        def traverse(x, y, refX, refY):
            if not check(x, y):
                return False
            if grid[x][y] == 0:
                return False
            grid[x][y] = 0
            self.shape += [(x - refX, y - refY)]
            traverse(x - 1, y, refX, refY)
            traverse(x + 1, y, refX, refY)
            traverse(x, y - 1, refX, refY)
            traverse(x, y + 1, refX, refY)

        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                self.shape = []
                traverse(row, col, row, col)
                if not self.shape:
                    continue
                if self.shape not in self.shapes:
                    result += 1
                    self.shapes += [self.shape]
        return result