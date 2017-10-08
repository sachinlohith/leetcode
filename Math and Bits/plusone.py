"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return map(int, list(str(int(''.join(str(x) for x in digits)) + 1)))


if __name__ == "__main__":
    sol = Solution()
    print sol.plusOne([1, 2, 3])
