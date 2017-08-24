"""
https://leetcode.com/problems/roman-to-integer/description/


Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for x in range(0, len(s) - 1):
            if romans[s[x]] < romans[s[x+1]]:
                result -= romans[s[x]]
            else:
                result += romans[s[x]]
        return result + romans[s[-1]]
