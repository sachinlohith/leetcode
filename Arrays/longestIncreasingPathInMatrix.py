"""
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/


Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""


class Solution(object):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        self.M, self.N = len(matrix), len(matrix[0])
        if self.N == 0:
            return 0
        self.dp = [[0 for _ in xrange(len(matrix[0]))] for _ in xrange(len(matrix))]

        def valid(x, y):
            return 0 <= x < self.M and 0 <= y < self.N

        def dfs(x, y):
            if self.dp[x][y] > 0:
                return self.dp[x][y]
            for i, j in self.directions:
                if valid(x + i, y + j) and matrix[x + i][y + j] > matrix[x][y]:
                    self.dp[x][y] = max(self.dp[x][y], dfs(x + i, y + j))
            self.dp[x][y] += 1
            return self.dp[x][y]

        res = 0
        for i in xrange(self.M):
            for j in xrange(self.N):
                res = max(res, dfs(i, j))
        return res

    """
        // Topological Sort Based Solution
        // An Alternative Solution
        public class Solution {
            private static final int[][] dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
            private int m, n;
            public int longestIncreasingPath(int[][] grid) {
                int m = grid.length;
                if (m == 0) return 0;
                int n = grid[0].length;
                // padding the matrix with zero as boundaries
                // assuming all positive integer, otherwise use INT_MIN as boundaries
                int[][] matrix = new int[m + 2][n + 2];
                for (int i = 0; i < m; ++i)
                    System.arraycopy(grid[i], 0, matrix[i + 1], 1, n);

                // calculate outdegrees
                int[][] outdegree = new int[m + 2][n + 2];
                for (int i = 1; i <= m; ++i)
                    for (int j = 1; j <= n; ++j)
                        for (int[] d: dir)
                            if (matrix[i][j] < matrix[i + d[0]][j + d[1]])
                                outdegree[i][j]++;

                // find leaves who have zero out degree as the initial level
                n += 2;
                m += 2;
                List<int[]> leaves = new ArrayList<>();
                for (int i = 1; i < m - 1; ++i)
                    for (int j = 1; j < n - 1; ++j)
                        if (outdegree[i][j] == 0) leaves.add(new int[]{i, j});

                // remove leaves level by level in topological order
                int height = 0;
                while (!leaves.isEmpty()) {
                    height++;
                    List<int[]> newLeaves = new ArrayList<>();
                    for (int[] node : leaves) {
                        for (int[] d:dir) {
                            int x = node[0] + d[0], y = node[1] + d[1];
                            if (matrix[node[0]][node[1]] > matrix[x][y])
                                if (--outdegree[x][y] == 0)
                                    newLeaves.add(new int[]{x, y});
                        }
                    }
                    leaves = newLeaves;
                }
                return height;
            }
        }
    """
