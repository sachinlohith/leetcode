"""
https://leetcode.com/problems/maximum-subarray/discuss/


Find the contiguous subarray within an array (containing at least one number)
which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using
the divide and conquer approach, which is more subtle.
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = [nums[0]]
        maxSum = cache[0]
        for idx in range(1, len(nums)):
            cache.append(nums[idx] + (cache[idx - 1] if cache[idx - 1] > 0 else 0))
            maxSum = max(maxSum, cache[idx])
        return maxSum

     def maxSubArrayHelper(self,nums, l, r):
        if l > r:
            return -2147483647
        m = (l+r) / 2

        leftMax = sumNum = 0
        for i in range(m - 1, l - 1, -1):
            sumNum += nums[i]
            leftMax = max(leftMax, sumNum)

        rightMax = sumNum = 0
        for i in range(m + 1, r + 1):
            sumNum += nums[i]
            rightMax = max(rightMax, sumNum)

        leftAns = self.maxSubArrayHelper(nums, l, m - 1)
        rightAns = self.maxSubArrayHelper(nums, m + 1, r)

        return max(leftMax + nums[m] + rightMax, max(leftAns, rightAns))

     def maxSubArrayDnC(self, nums):
        return self.maxSubArrayHelper(nums, 0, len(nums) - 1)
