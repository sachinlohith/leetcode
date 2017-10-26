"""
https://leetcode.com/problems/palindrome-permutation/description/


Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.
"""


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        from collections import Counter
        return len(filter(lambda x: x % 2 == 1, Counter(s).values())) <= 1