"""
https://leetcode.com/problems/next-greater-element-i/#/description
"""


class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        return map(
            lambda x: filter(lambda y: y > x, nums[nums.index(x) + 1:])[0] if
            filter(
                lambda y: y > x, nums[nums.index(x) + 1:]) else -1, findNums)

    def _nextGreaterElement(self, findNums, nums):
        d = {}
        st = []
        ans = []
        for x in nums:
            while len(st) and st[-1] < x:
                d[st.pop()] = x
            st.append(x)

        for x in findNums:
            ans.append(d.get(x, -1))
        return ans
