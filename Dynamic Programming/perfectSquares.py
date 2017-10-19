"""
https://leetcode.com/problems/perfect-squares/discuss/



"""


import sys

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        dp = [sys.maxint for _ in xrange(n + 1)]
        dp[0] = 0
        for i in xrange(1, n + 1):
            cur = 0
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j*j] + 1)
                j = j + 1
        return dp[-1]