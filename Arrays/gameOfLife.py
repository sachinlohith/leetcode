"""
https://leetcode.com/problems/game-of-life/discuss/


According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up:
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])

        def liveNeighbors(i, j):
            lives = 0
            x = max(i - 1, 0)
            minRow = min(i + 1, m - 1)
            while x <= minRow:
                y = max(j - 1, 0)
                minCol = min(j + 1, n - 1)
                while y <= minCol:
                    lives += (board[x][y] & 1)
                    y += 1
                x += 1
            lives -= (board[i][j] & 1)
            return lives

        for i in xrange(m):
            for j in xrange(n):
                lives = liveNeighbors(i, j)
                if board[i][j] == 1 and lives >= 2 and lives <= 3:
                    board[i][j] = 3
                if board[i][j] == 0 and lives == 3:
                    board[i][j] = 2

        for i in xrange(m):
            for j in xrange(n):
                board[i][j] = board[i][j] >> 1

