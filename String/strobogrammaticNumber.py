"""
https://leetcode.com/problems/strobogrammatic-number/description/


A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.

"""


class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        nMap = {'1':'1', '6':'9', '9':'6', '8':'8', '0':'0'}
        res = ''
        for n in str(num):
            if n not in nMap:
                return False
            res += nMap[n]
        return res[::-1] == num

    def isStrobogrammaticOneLiner(self, num):
        return all(num[i] + num[~i] in '696 00 11 88' for i in range(len(num) / 2 + 1))