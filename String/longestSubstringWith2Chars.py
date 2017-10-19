"""
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/


Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

For example, Given s = “eceba”,

T is "ece" which its length is 3.
"""


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        left, res, run = 0, 0, 0
        cMap = defaultdict(int)
        for char in s:
            cMap[char] += 1
            run += 1
            while len(cMap) > 2:
                cMap[s[left]] -= 1
                if cMap[s[left]] == 0:
                    del cMap[s[left]]
                left += 1
            if run - left > res:
                res = run - left
        return res