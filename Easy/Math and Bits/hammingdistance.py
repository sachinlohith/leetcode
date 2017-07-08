"""
https://leetcode.com/problems/hamming-distance/#/description
"""

class Solution(object):
    def hammingDistance(self, x, y):
        return bin(x ^ y).count('1')
