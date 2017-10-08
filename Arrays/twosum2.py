"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/#/description


Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1

    def twoSum2(self, numbers, target):
        # dictionary
        dic = {}
        for i, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target - num] + 1, i + 1]
            dic[num] = i

    def twoSum3(self, numbers, target):
        # binary search
        for i in xrange(len(numbers)):
            left, right = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp:
                    left = mid + 1
                else:
                    right = mid - 1
