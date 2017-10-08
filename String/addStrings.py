"""
https://leetcode.com/problems/add-strings/discuss/

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        from itertools import izip_longest
        z = izip_longest(num1[::-1], num2[::-1], fillvalue='0')
        res, zero, carry = [], 2 * ord('0'), 0
        for x in z:
            num = ord(x[0]) + ord(x[1]) - zero + carry
            res.append(str(num % 10))
            carry = num // 10
        return ('1' if carry else '') + ''.join(res[::-1])
