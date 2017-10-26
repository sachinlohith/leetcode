"""
https://leetcode.com/problems/walls-and-gates/description/


You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""


class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """

        self.DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.EMPTY = 2147483647
        self.GATE = 0
        self.WALL = 1
        self.M = len(rooms)
        self.N = len(rooms[0]) if self.M else 0

        from collections import deque

        queue = deque([])
        for i in xrange(self.M):
            for j in xrange(self.N):
                if rooms[i][j] == self.GATE:
                    queue.append((i, j))

        while queue:
            row, col = queue.popleft()
            for m, n in self.DIRECTIONS:
                r, c = row + m, col + n
                if r < 0 or r >= self.M or c < 0 or c >= self.N or rooms[r][c] != self.EMPTY:
                    continue
                rooms[r][c] = rooms[row][col] + 1
                queue.append((r, c))
