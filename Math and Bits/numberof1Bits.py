"""
https://leetcode.com/problems/number-of-1-bits/description/


Write a function that takes an unsigned integer and returns the number of ’1'
bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation
00000000000000000000000000001011, so the function should return 3.
"""


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n > 1:
            result += (n % 2 == 1)
            n = n / 2
        return result + 1 if n == 1 else result

    def hammingWeightOpt(self, n):
        res = 0
        while n != 0:
            res += 1
            n &= (n - 1)
        return res
