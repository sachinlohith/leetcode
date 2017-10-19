"""
https://leetcode.com/problems/power-of-four/description/


Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
"""


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        if num == 1:
            return True
        for i in xrange(0, 32, 2):
            if num == (4 << i):
                return True
        return False

    def isPowerOfFour(self, num):
        return num != 0 and num & (num - 1) == 0 and num & 1431655765 == num
