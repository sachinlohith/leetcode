"""
https://leetcode.com/problems/reshape-the-matrix/#/description
"""

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        newNums = [y for x in nums for y in x]
        return [newNums[(i*c):(i*c + c)] for i in xrange(r)] if r*c <= len(newNums) else nums