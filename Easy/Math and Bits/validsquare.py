"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

    Example 1:
        Input: 16
        Returns: True

    Example 2:
        Input: 14
        Returns: False
"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        ans = 1
        while ans*ans < num:
            ans += 1
        return True if ans*ans == num else False


if __name__ == "__main__":
    sol = Solution()
    print sol.isPerfectSquare(14)
