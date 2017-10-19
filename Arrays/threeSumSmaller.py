"""
https://leetcode.com/problems/3sum-smaller/description/


Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

For example, given nums = [-2, 0, 1, 3], and target = 2.

Return 2. Because there are two triplets which sums are less than 2:

[-2, 0, 1]
[-2, 0, 3]
Follow up:
Could you solve it in O(n2) runtime?
"""


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def twoSumSmaller(self, start, target):
            ans = 0
            left = start
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < target:
                    ans += right - left
                    left += 1
                else:
                    right -= 1
            return ans
        nums.sort()
        return sum(twoSumSmaller(nums, i + 1, target - nums[i]) for i in xrange(0, len(nums) - 2))