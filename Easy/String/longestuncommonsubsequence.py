"""
https://leetcode.com/problems/longest-uncommon-subsequence-i/#/description
"""


class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if len(a) < len(b):
            a, b = b, a
        for x in range(len(a)):
            if a[x:] not in b:
                return len(a[x:])
        return -1
