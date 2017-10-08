"""
https://leetcode.com/problems/excel-sheet-column-number/description/


Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        import string
        alphabets = ' ' + string.ascii_uppercase
        place = len(s) - 1
        result = 0
        for letter in s[:-1]:
            result += ((26 ** place) * alphabets.index(letter))
            place -= 1
        return result + alphabets.index(s[-1])
