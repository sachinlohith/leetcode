"""
https://leetcode.com/problems/missing-number/description/


Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return min(set(range(max(nums) + 2)) - set(nums))


    def missingNumberOpt(self, nums):
        n = len(nums)
        return n * (n+1) / 2 - sum(nums)


    def missingNumberXOR(self, nums):
        return reduce(operator.xor, nums + range(len(nums)+1))
