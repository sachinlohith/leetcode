"""
https://leetcode.com/problems/add-digits/#/description
"""


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num / 10 != 0:
            num = sum(map(int, list(str(num))))
        return num

    def optimalAddDigits(self, num):
        return 0 if num == 0 else (num - 1) % 9 + 1
