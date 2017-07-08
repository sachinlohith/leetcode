"""
https://leetcode.com/problems/combination-sum-iv/#/description
"""

class Solution(object):
    def combinationSum4(self, nums, target):
        dp = [1] + [0] * target
        for i in xrange(1, target+1):
            for j in xrange(len(nums)):
                if i - nums[j] >= 0:
                    dp[i] += dp[i - nums[j]]
        return dp[target]
