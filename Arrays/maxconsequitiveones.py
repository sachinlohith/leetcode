"""
https://leetcode.com/problems/max-consecutive-ones/#/description
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        run = 0
        for x in range(len(nums)):
            if nums[x] == 1:
                run += 1
            else:
                if result < run:
                    result = run
                run = 0
        return result if result > run else run
