"""
https://leetcode.com/problems/number-complement/#/description
"""


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int(''.join('1' if x == '0' else '0' for x in bin(num)[2:]), 2)

sol = Solution()
print sol.findComplement(5)