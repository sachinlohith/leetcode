"""
https://leetcode.com/problems/longest-palindrome/description/

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        counter = Counter(s).items()
        result = filter(lambda x: x[1] % 2 == 0, counter)
        answer = sum(map(lambda x: x[1], result))
        temp = list(set(counter) - set(result))
        if temp != []:
            return answer + sum(map(lambda x: x[1], temp)) - len(temp) + 1
        return answer

    def longestPalindromeOpt(self, s):
        import collections
        odds = sum(v & 1 for v in collections.Counter(s).values())
        return len(s) - odds + bool(odds)
