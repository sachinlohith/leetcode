"""
https://leetcode.com/problems/island-perimeter/#/description
"""


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def isValidCell(x, y, xsize, ysize):
            return True if (x >= 0 and x <= xsize - 1) and (y >= 0 and y <= ysize - 1) else False

        def getCellPerimeter(x, y, grid, xsize, ysize):
            result = 0
            if isValidCell(x+1, y, xsize, ysize):
                result += 1 - grid[x+1][y]
            else:
                result += 1
            if isValidCell(x-1, y, xsize, ysize):
                result += 1 - grid[x-1][y]
            else:
                result += 1
            if isValidCell(x, y+1, xsize, ysize):
                result += 1 - grid[x][y+1]
            else:
                result += 1
            if isValidCell(x, y-1, xsize, ysize):
                result += 1 - grid[x][y-1]
            else:
                result += 1
            return result
        
        result = 0
        for x in xrange(len(grid)):
            for y in xrange(len(grid[x])):
                if grid[x][y] == 1:
                    result += getCellPerimeter(x, y, grid, len(grid), len(grid[x]))
        return result

    def optimalIslandPerimeter(self, grid):
        import operator
        return (sum(sum(map(operator.ne, [0] + row, row + [0]))
            for row in grid + map(list, zip(*grid))))
