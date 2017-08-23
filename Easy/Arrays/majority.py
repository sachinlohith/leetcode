"""
https://leetcode.com/problems/majority-element/description/


Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        result = Counter(nums)
        major = len(nums) // 2
        return filter(lambda x: result[x] > major, result)[0]
