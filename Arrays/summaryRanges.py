"""
https://leetcode.com/problems/summary-ranges/description/

Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
Input: [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Example 2:
Input: [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        result = []
        left, right = str(nums[0]), str(nums[0])
        for idx in xrange(1, len(nums)):
            if nums[idx] != nums[idx - 1] + 1:
                result.append((left, left + '->' + right)[left != right])
                left = str(nums[idx])
            right = str(nums[idx])
        result.append((left, left + '->' + right)[left != right])
        return result