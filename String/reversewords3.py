"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/#/description
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(map(lambda x: x[::-1], s.split()))
