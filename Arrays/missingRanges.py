"""
https://leetcode.com/problems/missing-ranges/description/


Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
"""


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if not nums:
            if upper > lower:
                return [str(lower) + '->' + str(upper)]
            else:
                return [str(lower)]
        prev = 0
        i = 1
        result = []
        if nums[prev] > lower:
            if nums[prev] - lower == 1:
                result.append(str(lower))
            else:
                result.append(str(lower) + '->' + str(nums[prev] - 1))
        while i < len(nums):
            if nums[i] - nums[prev] > 1:
                if nums[i] - nums[prev] == 2:
                    result.append(str(nums[prev] + 1))
                else:
                    result.append(str(nums[prev] + 1) + '->' + str(nums[i] - 1))
            i += 1
            prev += 1
        if nums[prev] < upper:
            if upper - nums[prev] == 1:
                result.append(str(nums[prev] + 1))
            else:
                result.append(str(nums[prev] + 1) + '->' + str(upper))
        return result

    def findMissingRangesOpt(self, nums, lower, upper):
        result = []
        A.append(upper + 1)
        pre = lower - 1
        for i in A:
            if (i == pre + 2):
                result.append(str(i - 1))
            elif (i > pre + 2):
                result.append(str(pre + 1) + "->" + str(i - 1))
            pre = i
        return result