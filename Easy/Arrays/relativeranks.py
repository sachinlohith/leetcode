"""
https://leetcode.com/problems/relative-ranks/description/


Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal".
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.
"""


class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranks = {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}
        for index, player in enumerate(sorted(nums, reverse=True)):
            if index + 1 in ranks:
                nums[nums.index(player)] = ranks[index + 1]
            else:
                nums[nums.index(player)] = str(index + 1)
        return nums


    def findRelativeRanksOpt(self, nums):
        sort = sorted(nums)[::-1]
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + map(str, range(4, len(nums) + 1))
        mapping = dict(zip(sort, rank))
        return map(mapping.get, nums)
