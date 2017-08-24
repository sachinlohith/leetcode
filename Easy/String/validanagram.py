"""
https://leetcode.com/problems/valid-anagram/description/

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return not any([s.count(x) != t.count(x) for x in list(set(s)) + list(set(t))])

    def isAnagramOpt1(self, s, t):
        return sorted(s) == sorted(t)

    def isAnagramOpt2(self, s, t):
        from collections import Counter
        return Counter(s) == Counter(t)
