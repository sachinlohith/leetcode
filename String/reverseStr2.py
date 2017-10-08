"""
https://leetcode.com/problems/reverse-string-ii/description/


Given a string and an integer k, you need to reverse the first k characters for
every 2k characters counting from the start of the string. If there are less
than k characters left, reverse all of them. If there are less than 2k but
greater than or equal to k characters, then reverse the first k characters and
left the other as original.

Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
"""


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = ""
        for i in range(0, len(s), 2*k):
            result += s[i + k - 1:i:-1] + s[i]
            result += s[i + k:i + (2 * k)]
        return result

    def reverseStrRecurse(self, s, k):
        return s[:k][::-1] + s[k:2*k] + self.reverseStrRecurse(s[2*k:], k) if s else ""
