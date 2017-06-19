'''
https://leetcode.com/problems/guess-number-higher-or-lower/#/description

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

    -1 : My number is lower
    1 : My number is higher
    0 : Congrats! You got it!
Example:
    n = 10, I pick 6.

    Return 6.
'''

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        while True:
            if guess((low + high) / 2) == 0:
                return (low + high) / 2
            elif guess((low + high) / 2) == -1:
                high = (low + high) / 2
            else:
                low = (low + high) / 2

