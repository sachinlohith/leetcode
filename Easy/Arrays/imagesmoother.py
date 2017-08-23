"""
https://leetcode.com/problems/image-smoother/description/

Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].
"""


class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(M)
        cols = len(M[rows - 1])

        def isValidCell((x, y)):
            return x >= 0 and x < rows and y >= 0 and y < cols

        def getAdjacentCells(x, y):
            return map(lambda (x, y): M[x][y], filter(isValidCell, [
                (x, y),
                (x + 1, y + 1),
                (x + 1, y - 1),
                (x - 1, y + 1),
                (x - 1, y - 1),
                (x, y + 1),
                (x, y - 1),
                (x - 1, y),
                (x + 1, y)
            ]))

        result = []
        for i in range(rows):
            temp = []
            for j in range(cols):
                adj = getAdjacentCells(i, j)
                temp.append(sum(adj) // len(adj))
            result += [temp]
        return result
