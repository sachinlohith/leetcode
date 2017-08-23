"""
https://leetcode.com/problems/first-unique-character-in-a-string/description/


Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        for i, x in enumerate(s[:-1]):
            if x not in s[i + 1:] and x not in s[:i]:
                return i
        return len(s) - 1 if s[-1] not in s[:-1] else -1

    def firstUniqCharOpt(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1
