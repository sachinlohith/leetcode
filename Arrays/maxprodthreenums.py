"""
https://leetcode.com/problems/maximum-product-of-three-numbers/discuss/

Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
"""


class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import sys
        p = q = r = -sys.maxint - 1
        s = t = sys.maxint
        for num in nums:
            if num > p:
                p, q, r = num, p, q
            elif num > q:
                q, r = num, q
            elif num > r:
                r = num
            if num < s:
                s, t = num, s
            elif num < t:
                t = num
        return max(p * q * r, p * s * t)
