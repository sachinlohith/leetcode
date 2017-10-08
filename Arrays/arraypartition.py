"""https://leetcode.com/problems/array-partition-i/#/description."""


class Solution(object):
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])
