"""
https://leetcode.com/problems/set-mismatch/discuss/

The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.
"""


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        counter = [0] * (N + 1)
        for x in nums:
            counter[x] += 1
        twice = None
        never = None
        for x in range(1, N + 1):
            if counter[x] == 2:
                twice = x
            if counter[x] == 0:
                never = x
        return twice, never

    def findErrorNumsNew(self, nums):
        N = len(A)
        alpha = sum(A) - N*(N+1)/2
        beta = (sum(x*x for x in A) - N*(N+1)*(2*N+1)/6) / alpha
        return (alpha + beta) / 2, (beta - alpha) / 2
